"""
RTI Application Tracker

Track filed RTI applications with deadlines, status updates, and appeal management.
Uses SQLAlchemy for local database storage.

Key deadlines under RTI Act, 2005:
- Response: 30 days from filing (Section 7(1))
- Life/liberty matters: 48 hours (Section 7(1))
- Transfer to other authority: 5 days (Section 6(3))
- First Appeal: Within 30 days of non-response/refusal (Section 19(1))
- Second Appeal to CIC/SIC: Within 90 days of first appeal decision (Section 19(3))
- Penalty on PIO: Rs. 250/day, max Rs. 25,000 (Section 20)
"""

import json
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Optional

from sqlalchemy import (
    Column,
    DateTime,
    Enum as SAEnum,
    Integer,
    String,
    Text,
    Boolean,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    pass


class RTIStatus(str, Enum):
    DRAFTED = "drafted"
    FILED = "filed"
    ACKNOWLEDGED = "acknowledged"
    TRANSFERRED = "transferred"  # Section 6(3) transfer
    RESPONSE_RECEIVED = "response_received"
    PARTIAL_RESPONSE = "partial_response"
    DENIED = "denied"
    NO_RESPONSE = "no_response"  # deadline passed
    FIRST_APPEAL_FILED = "first_appeal_filed"
    FIRST_APPEAL_DECIDED = "first_appeal_decided"
    SECOND_APPEAL_FILED = "second_appeal_filed"
    SECOND_APPEAL_DECIDED = "second_appeal_decided"
    COMPLAINT_FILED = "complaint_filed"  # Section 18 complaint to CIC/SIC
    CLOSED = "closed"


class RTIRecord(Base):
    """Database model for a tracked RTI application."""

    __tablename__ = "rti_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    reference_number = Column(String(100), unique=True, nullable=True)
    agency_code = Column(String(20), nullable=False)
    agency_name = Column(String(200), nullable=False)
    pio_name = Column(String(200), nullable=True)
    pio_address = Column(Text, nullable=True)

    applicant_name = Column(String(200), nullable=False)
    subject = Column(Text, nullable=False)
    questions_json = Column(Text, nullable=False)  # JSON list of questions
    full_text = Column(Text, nullable=True)

    state = Column(String(100), nullable=True)
    district = Column(String(100), nullable=True)

    filing_date = Column(DateTime, nullable=False)
    fee_amount = Column(Integer, default=10)
    fee_mode = Column(String(50), nullable=True)  # IPO, DD, online, etc.
    fee_receipt = Column(String(100), nullable=True)

    status = Column(SAEnum(RTIStatus), default=RTIStatus.DRAFTED)
    is_bpl = Column(Boolean, default=False)

    # Tracking dates
    acknowledgment_date = Column(DateTime, nullable=True)
    response_date = Column(DateTime, nullable=True)
    transfer_date = Column(DateTime, nullable=True)
    transferred_to = Column(String(200), nullable=True)

    # Deadlines (auto-calculated but stored for queries)
    response_deadline = Column(DateTime, nullable=False)
    first_appeal_deadline = Column(DateTime, nullable=True)
    second_appeal_deadline = Column(DateTime, nullable=True)

    # Appeal tracking
    first_appeal_date = Column(DateTime, nullable=True)
    first_appeal_authority = Column(String(200), nullable=True)
    first_appeal_decision_date = Column(DateTime, nullable=True)
    first_appeal_outcome = Column(Text, nullable=True)

    second_appeal_date = Column(DateTime, nullable=True)
    second_appeal_authority = Column(String(200), nullable=True)
    second_appeal_decision_date = Column(DateTime, nullable=True)
    second_appeal_outcome = Column(Text, nullable=True)

    # Notes
    notes = Column(Text, nullable=True)
    response_summary = Column(Text, nullable=True)
    documents_received = Column(Text, nullable=True)  # JSON list of doc descriptions

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class RTITracker:
    """
    Track RTI applications, deadlines, and appeal status.

    Manages the full lifecycle of RTI applications from drafting through
    response and appeals.
    """

    def __init__(self, db_path: Optional[str] = None):
        if db_path is None:
            db_path = str(Path.home() / ".india_toolkit" / "rti_tracker.db")
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.engine = create_engine(f"sqlite:///{db_path}")
        Base.metadata.create_all(self.engine)
        self.SessionLocal = sessionmaker(bind=self.engine)

    def _get_session(self) -> Session:
        return self.SessionLocal()

    def add_rti(
        self,
        agency_code: str,
        agency_name: str,
        applicant_name: str,
        subject: str,
        questions: list[str],
        filing_date: Optional[datetime] = None,
        fee_amount: int = 10,
        state: Optional[str] = None,
        district: Optional[str] = None,
        full_text: Optional[str] = None,
        reference_number: Optional[str] = None,
        **kwargs,
    ) -> int:
        """Add a new RTI to the tracker. Returns record ID."""
        if filing_date is None:
            filing_date = datetime.now()

        response_deadline = filing_date + timedelta(days=30)

        record = RTIRecord(
            reference_number=reference_number,
            agency_code=agency_code,
            agency_name=agency_name,
            applicant_name=applicant_name,
            subject=subject,
            questions_json=json.dumps(questions, ensure_ascii=False),
            full_text=full_text,
            filing_date=filing_date,
            fee_amount=fee_amount,
            response_deadline=response_deadline,
            state=state,
            district=district,
            status=RTIStatus.FILED if filing_date else RTIStatus.DRAFTED,
            **kwargs,
        )

        with self._get_session() as session:
            session.add(record)
            session.commit()
            return record.id

    def update_status(
        self,
        record_id: int,
        status: RTIStatus,
        notes: Optional[str] = None,
        response_summary: Optional[str] = None,
    ) -> bool:
        """Update RTI status."""
        with self._get_session() as session:
            record = session.get(RTIRecord, record_id)
            if not record:
                return False
            record.status = status
            record.updated_at = datetime.utcnow()
            if notes:
                existing = record.notes or ""
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                record.notes = f"{existing}\n[{timestamp}] {notes}".strip()
            if response_summary:
                record.response_summary = response_summary
            if status == RTIStatus.RESPONSE_RECEIVED:
                record.response_date = datetime.now()
            session.commit()
            return True

    def mark_response_received(
        self,
        record_id: int,
        response_summary: str,
        documents: Optional[list[str]] = None,
        response_date: Optional[datetime] = None,
    ) -> bool:
        """Mark RTI as having received a response."""
        with self._get_session() as session:
            record = session.get(RTIRecord, record_id)
            if not record:
                return False
            record.status = RTIStatus.RESPONSE_RECEIVED
            record.response_date = response_date or datetime.now()
            record.response_summary = response_summary
            if documents:
                record.documents_received = json.dumps(documents, ensure_ascii=False)
            record.updated_at = datetime.utcnow()
            session.commit()
            return True

    def file_first_appeal(
        self,
        record_id: int,
        appeal_authority: str,
        appeal_date: Optional[datetime] = None,
        notes: Optional[str] = None,
    ) -> bool:
        """Record filing of first appeal under Section 19(1)."""
        with self._get_session() as session:
            record = session.get(RTIRecord, record_id)
            if not record:
                return False
            record.status = RTIStatus.FIRST_APPEAL_FILED
            record.first_appeal_date = appeal_date or datetime.now()
            record.first_appeal_authority = appeal_authority
            # Second appeal deadline: 90 days after first appeal decision
            record.first_appeal_deadline = record.first_appeal_date + timedelta(days=30)
            if notes:
                existing = record.notes or ""
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                record.notes = f"{existing}\n[{timestamp}] First appeal: {notes}".strip()
            record.updated_at = datetime.utcnow()
            session.commit()
            return True

    def file_second_appeal(
        self,
        record_id: int,
        appeal_date: Optional[datetime] = None,
        commission: str = "Central Information Commission",
        notes: Optional[str] = None,
    ) -> bool:
        """Record filing of second appeal under Section 19(3) to CIC/SIC."""
        with self._get_session() as session:
            record = session.get(RTIRecord, record_id)
            if not record:
                return False
            record.status = RTIStatus.SECOND_APPEAL_FILED
            record.second_appeal_date = appeal_date or datetime.now()
            record.second_appeal_authority = commission
            record.second_appeal_deadline = record.second_appeal_date + timedelta(days=90)
            if notes:
                existing = record.notes or ""
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                record.notes = f"{existing}\n[{timestamp}] Second appeal: {notes}".strip()
            record.updated_at = datetime.utcnow()
            session.commit()
            return True

    def get_overdue(self) -> list[dict]:
        """Get all RTIs that are past their response deadline without response."""
        now = datetime.now()
        with self._get_session() as session:
            records = (
                session.query(RTIRecord)
                .filter(
                    RTIRecord.response_deadline < now,
                    RTIRecord.status.in_([RTIStatus.FILED, RTIStatus.ACKNOWLEDGED]),
                )
                .all()
            )
            return [self._record_to_dict(r) for r in records]

    def get_upcoming_deadlines(self, days: int = 7) -> list[dict]:
        """Get RTIs with deadlines in the next N days."""
        now = datetime.now()
        cutoff = now + timedelta(days=days)
        with self._get_session() as session:
            records = (
                session.query(RTIRecord)
                .filter(
                    RTIRecord.response_deadline >= now,
                    RTIRecord.response_deadline <= cutoff,
                    RTIRecord.status.in_([RTIStatus.FILED, RTIStatus.ACKNOWLEDGED]),
                )
                .all()
            )
            return [self._record_to_dict(r) for r in records]

    def get_all(self, status: Optional[RTIStatus] = None) -> list[dict]:
        """Get all RTIs, optionally filtered by status."""
        with self._get_session() as session:
            query = session.query(RTIRecord)
            if status:
                query = query.filter(RTIRecord.status == status)
            records = query.order_by(RTIRecord.filing_date.desc()).all()
            return [self._record_to_dict(r) for r in records]

    def get_by_id(self, record_id: int) -> Optional[dict]:
        """Get a single RTI record."""
        with self._get_session() as session:
            record = session.get(RTIRecord, record_id)
            if record:
                return self._record_to_dict(record)
            return None

    def get_by_agency(self, agency_code: str) -> list[dict]:
        """Get all RTIs for a specific agency."""
        with self._get_session() as session:
            records = (
                session.query(RTIRecord)
                .filter(RTIRecord.agency_code == agency_code)
                .order_by(RTIRecord.filing_date.desc())
                .all()
            )
            return [self._record_to_dict(r) for r in records]

    def get_stats(self) -> dict:
        """Get summary statistics."""
        with self._get_session() as session:
            total = session.query(RTIRecord).count()
            by_status = {}
            for status in RTIStatus:
                count = (
                    session.query(RTIRecord)
                    .filter(RTIRecord.status == status)
                    .count()
                )
                if count > 0:
                    by_status[status.value] = count

            overdue = len(self.get_overdue())
            upcoming = len(self.get_upcoming_deadlines(7))

            return {
                "total": total,
                "by_status": by_status,
                "overdue": overdue,
                "upcoming_deadlines_7d": upcoming,
            }

    def _record_to_dict(self, record: RTIRecord) -> dict:
        """Convert RTI record to dictionary."""
        return {
            "id": record.id,
            "reference_number": record.reference_number,
            "agency_code": record.agency_code,
            "agency_name": record.agency_name,
            "applicant_name": record.applicant_name,
            "subject": record.subject,
            "questions": json.loads(record.questions_json),
            "state": record.state,
            "district": record.district,
            "filing_date": record.filing_date.isoformat() if record.filing_date else None,
            "fee_amount": record.fee_amount,
            "status": record.status.value if record.status else None,
            "response_deadline": record.response_deadline.isoformat() if record.response_deadline else None,
            "response_date": record.response_date.isoformat() if record.response_date else None,
            "response_summary": record.response_summary,
            "first_appeal_date": record.first_appeal_date.isoformat() if record.first_appeal_date else None,
            "first_appeal_deadline": record.first_appeal_deadline.isoformat() if record.first_appeal_deadline else None,
            "second_appeal_date": record.second_appeal_date.isoformat() if record.second_appeal_date else None,
            "notes": record.notes,
            "days_since_filing": (datetime.now() - record.filing_date).days if record.filing_date else None,
            "is_overdue": (
                datetime.now() > record.response_deadline
                and record.status in (RTIStatus.FILED, RTIStatus.ACKNOWLEDGED)
            ) if record.response_deadline else False,
        }

    def export_json(self, filepath: Optional[str] = None) -> str:
        """Export all records as JSON."""
        records = self.get_all()
        data = json.dumps(records, indent=2, ensure_ascii=False)
        if filepath:
            Path(filepath).write_text(data, encoding="utf-8")
        return data
