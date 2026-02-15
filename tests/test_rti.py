"""
Tests for RTI Generator and Tracker.
"""

import json
import os
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from india.rti.rti_generator import (
    RTIGenerator,
    RTIApplication,
    AGENCY_DIRECTORY,
    FEES,
)
from india.rti.rti_tracker import RTITracker, RTIStatus


# ---- RTI Application Tests ----


class TestRTIApplication:
    """Test RTI application data model."""

    def test_default_filing_date(self):
        app = RTIApplication(
            agency_code="awbi",
            questions=["Test question"],
            applicant_name="Test Applicant",
            applicant_address="Test Address",
        )
        assert app.filing_date is not None
        assert isinstance(app.filing_date, datetime)

    def test_fee_amount_central(self):
        app = RTIApplication(
            agency_code="awbi",
            questions=["Test"],
            applicant_name="Test",
            applicant_address="Test",
        )
        assert app.fee_amount == 10

    def test_fee_amount_bpl(self):
        app = RTIApplication(
            agency_code="awbi",
            questions=["Test"],
            applicant_name="Test",
            applicant_address="Test",
            is_bpl=True,
        )
        assert app.fee_amount == 0

    def test_response_deadline(self):
        filing_date = datetime(2026, 1, 1)
        app = RTIApplication(
            agency_code="awbi",
            questions=["Test"],
            applicant_name="Test",
            applicant_address="Test",
            filing_date=filing_date,
        )
        assert app.response_deadline == datetime(2026, 1, 31)

    def test_first_appeal_deadline(self):
        filing_date = datetime(2026, 1, 1)
        app = RTIApplication(
            agency_code="awbi",
            questions=["Test"],
            applicant_name="Test",
            applicant_address="Test",
            filing_date=filing_date,
        )
        # 30 days response + 30 days appeal window
        assert app.first_appeal_deadline == datetime(2026, 3, 2)

    def test_second_appeal_deadline(self):
        filing_date = datetime(2026, 1, 1)
        app = RTIApplication(
            agency_code="awbi",
            questions=["Test"],
            applicant_name="Test",
            applicant_address="Test",
            filing_date=filing_date,
        )
        # first_appeal_deadline + 90 days
        expected = app.first_appeal_deadline + timedelta(days=90)
        assert app.second_appeal_deadline == expected


# ---- RTI Generator Tests ----


class TestRTIGenerator:
    """Test RTI generation."""

    def setup_method(self):
        self.generator = RTIGenerator()

    def test_list_agencies(self):
        agencies = self.generator.list_agencies()
        assert "awbi" in agencies
        assert "fssai" in agencies
        assert "cpcb" in agencies
        assert "dahd" in agencies
        assert "nlm" in agencies
        assert "rgm" in agencies

    def test_get_agency_info(self):
        info = self.generator.get_agency_info("awbi")
        assert info["name"] == "Animal Welfare Board of India"
        assert "Chennai" in info["address"]
        assert info["fee_category"] == "central"

    def test_get_agency_info_unknown(self):
        info = self.generator.get_agency_info("unknown")
        assert info == {}

    def test_generate_english(self):
        app = RTIApplication(
            agency_code="awbi",
            questions=[
                "What inspection reports exist for XYZ Farm?",
                "What is the compliance status?",
            ],
            applicant_name="Test Advocate",
            applicant_address="123 Test Street, New Delhi - 110001",
            subject="Inspection reports for XYZ Farm",
        )
        text = self.generator.generate(app)

        assert "SECTION 6(1)" in text
        assert "RIGHT TO INFORMATION ACT, 2005" in text
        assert "Animal Welfare Board of India" in text
        assert "Test Advocate" in text
        assert "XYZ Farm" in text
        assert "Rs. 10" in text
        assert "30 days" in text

    def test_generate_hindi(self):
        app = RTIApplication(
            agency_code="awbi",
            questions=["निरीक्षण रिपोर्ट दें"],
            applicant_name="टेस्ट",
            applicant_address="टेस्ट पता",
            language="hindi",
        )
        text = self.generator.generate(app)

        assert "धारा 6(1)" in text
        assert "सूचना का अधिकार" in text
        assert "भारतीय पशु कल्याण बोर्ड" in text

    def test_generate_bilingual(self):
        app = RTIApplication(
            agency_code="fssai",
            questions=["Test question"],
            applicant_name="Test",
            applicant_address="Test Address",
            language="bilingual",
        )
        text = self.generator.generate(app)

        assert "ENGLISH VERSION" in text
        assert "हिंदी संस्करण" in text

    def test_generate_bpl_exempt(self):
        app = RTIApplication(
            agency_code="awbi",
            questions=["Test"],
            applicant_name="Test",
            applicant_address="Test",
            is_bpl=True,
            bpl_certificate_number="BPL/2025/12345",
        )
        text = self.generator.generate(app)

        assert "Below Poverty Line" in text
        assert "BPL/2025/12345" in text
        assert "exempt" in text.lower()

    def test_list_templates(self):
        templates = self.generator.list_templates()
        assert isinstance(templates, list)
        # Templates should exist in the rti_templates directory
        if templates:
            assert any("awbi" in t for t in templates)

    def test_awbi_inspection_request(self):
        app = self.generator.awbi_inspection_request(
            facility_name="ABC Poultry Farm",
            facility_location="Namakkal, Tamil Nadu",
            applicant_name="Test Advocate",
            applicant_address="Chennai",
        )
        assert app.agency_code == "awbi"
        assert len(app.questions) == 5
        assert "ABC Poultry Farm" in app.questions[0]
        assert "Namakkal" in app.questions[0]

    def test_fssai_violations_request(self):
        app = self.generator.fssai_violations_request(
            state="Maharashtra",
            district="Pune",
            applicant_name="Test",
            applicant_address="Test",
        )
        assert app.agency_code == "fssai"
        assert len(app.questions) == 5
        assert "Pune" in app.questions[0]
        assert "Maharashtra" in app.questions[0]

    def test_pollution_board_request(self):
        app = self.generator.pollution_board_request(
            state="Tamil Nadu",
            district="Namakkal",
            applicant_name="Test",
            applicant_address="Test",
        )
        assert app.agency_code == "cpcb"
        assert any("Namakkal" in q for q in app.questions)

    def test_subsidy_data_request_both(self):
        app = self.generator.subsidy_data_request(
            state="Gujarat",
            applicant_name="Test",
            applicant_address="Test",
            scheme="both",
        )
        assert app.agency_code == "dahd"
        # Should have questions about both NLM and RGM
        text = " ".join(app.questions)
        assert "National Livestock Mission" in text
        assert "Rashtriya Gokul Mission" in text

    def test_subsidy_data_request_nlm_only(self):
        app = self.generator.subsidy_data_request(
            state="Karnataka",
            applicant_name="Test",
            applicant_address="Test",
            scheme="nlm",
        )
        assert app.agency_code == "nlm"

    def test_slaughterhouse_license_request(self):
        app = self.generator.slaughterhouse_license_request(
            district="Chennai",
            state="Tamil Nadu",
            applicant_name="Test",
            applicant_address="Test",
        )
        assert app.agency_code == "fssai"
        assert len(app.questions) == 6
        assert any("Chennai" in q for q in app.questions)


# ---- RTI Tracker Tests ----


class TestRTITracker:
    """Test RTI tracking database."""

    def setup_method(self):
        # Use temporary database for tests
        self.tmp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.tmp_dir, "test_rti.db")
        self.tracker = RTITracker(db_path=self.db_path)

    def test_add_rti(self):
        record_id = self.tracker.add_rti(
            agency_code="awbi",
            agency_name="Animal Welfare Board of India",
            applicant_name="Test Advocate",
            subject="Test RTI",
            questions=["Question 1", "Question 2"],
        )
        assert record_id is not None
        assert record_id > 0

    def test_get_by_id(self):
        record_id = self.tracker.add_rti(
            agency_code="fssai",
            agency_name="FSSAI",
            applicant_name="Test",
            subject="Test FSSAI RTI",
            questions=["Q1"],
        )
        record = self.tracker.get_by_id(record_id)
        assert record is not None
        assert record["agency_code"] == "fssai"
        assert record["subject"] == "Test FSSAI RTI"
        assert record["questions"] == ["Q1"]

    def test_get_by_id_not_found(self):
        record = self.tracker.get_by_id(9999)
        assert record is None

    def test_update_status(self):
        record_id = self.tracker.add_rti(
            agency_code="awbi",
            agency_name="AWBI",
            applicant_name="Test",
            subject="Test",
            questions=["Q1"],
        )
        success = self.tracker.update_status(
            record_id, RTIStatus.ACKNOWLEDGED, notes="Received acknowledgment letter"
        )
        assert success is True

        record = self.tracker.get_by_id(record_id)
        assert record["status"] == "acknowledged"
        assert "acknowledgment letter" in record["notes"]

    def test_mark_response_received(self):
        record_id = self.tracker.add_rti(
            agency_code="cpcb",
            agency_name="CPCB",
            applicant_name="Test",
            subject="Pollution data",
            questions=["Q1"],
        )
        success = self.tracker.mark_response_received(
            record_id,
            response_summary="Received partial data for 2023-24",
            documents=["CTO list", "Effluent data"],
        )
        assert success is True

        record = self.tracker.get_by_id(record_id)
        assert record["status"] == "response_received"
        assert record["response_summary"] == "Received partial data for 2023-24"

    def test_file_first_appeal(self):
        record_id = self.tracker.add_rti(
            agency_code="awbi",
            agency_name="AWBI",
            applicant_name="Test",
            subject="Test",
            questions=["Q1"],
        )
        success = self.tracker.file_first_appeal(
            record_id,
            appeal_authority="Secretary, AWBI",
            notes="No response received within 30 days",
        )
        assert success is True

        record = self.tracker.get_by_id(record_id)
        assert record["status"] == "first_appeal_filed"

    def test_get_overdue(self):
        # Add an RTI with a past filing date (31+ days ago)
        old_date = datetime.now() - timedelta(days=35)
        self.tracker.add_rti(
            agency_code="awbi",
            agency_name="AWBI",
            applicant_name="Test",
            subject="Overdue RTI",
            questions=["Q1"],
            filing_date=old_date,
        )
        # Add a recent RTI
        self.tracker.add_rti(
            agency_code="fssai",
            agency_name="FSSAI",
            applicant_name="Test",
            subject="Recent RTI",
            questions=["Q1"],
            filing_date=datetime.now(),
        )

        overdue = self.tracker.get_overdue()
        assert len(overdue) == 1
        assert overdue[0]["subject"] == "Overdue RTI"

    def test_get_upcoming_deadlines(self):
        # Add RTI filing 25 days ago (deadline in 5 days)
        date_25_ago = datetime.now() - timedelta(days=25)
        self.tracker.add_rti(
            agency_code="awbi",
            agency_name="AWBI",
            applicant_name="Test",
            subject="Upcoming deadline",
            questions=["Q1"],
            filing_date=date_25_ago,
        )

        upcoming = self.tracker.get_upcoming_deadlines(7)
        assert len(upcoming) == 1

    def test_get_all(self):
        self.tracker.add_rti(
            agency_code="awbi",
            agency_name="AWBI",
            applicant_name="Test",
            subject="RTI 1",
            questions=["Q1"],
        )
        self.tracker.add_rti(
            agency_code="fssai",
            agency_name="FSSAI",
            applicant_name="Test",
            subject="RTI 2",
            questions=["Q1"],
        )

        all_records = self.tracker.get_all()
        assert len(all_records) == 2

    def test_get_by_agency(self):
        self.tracker.add_rti(
            agency_code="awbi",
            agency_name="AWBI",
            applicant_name="Test",
            subject="AWBI RTI",
            questions=["Q1"],
        )
        self.tracker.add_rti(
            agency_code="fssai",
            agency_name="FSSAI",
            applicant_name="Test",
            subject="FSSAI RTI",
            questions=["Q1"],
        )

        awbi_records = self.tracker.get_by_agency("awbi")
        assert len(awbi_records) == 1
        assert awbi_records[0]["agency_code"] == "awbi"

    def test_get_stats(self):
        self.tracker.add_rti(
            agency_code="awbi",
            agency_name="AWBI",
            applicant_name="Test",
            subject="Test",
            questions=["Q1"],
        )
        stats = self.tracker.get_stats()
        assert stats["total"] == 1
        assert "filed" in stats["by_status"]

    def test_export_json(self):
        self.tracker.add_rti(
            agency_code="awbi",
            agency_name="AWBI",
            applicant_name="Test",
            subject="Export test",
            questions=["Q1"],
        )

        export_path = os.path.join(self.tmp_dir, "export.json")
        data = self.tracker.export_json(export_path)

        assert os.path.exists(export_path)
        parsed = json.loads(data)
        assert len(parsed) == 1
        assert parsed[0]["subject"] == "Export test"


# ---- Agency Directory Tests ----


class TestAgencyDirectory:
    """Test agency directory data integrity."""

    def test_all_agencies_have_required_fields(self):
        required_fields = ["name", "pio_designation", "address", "fee_category"]
        for code, agency in AGENCY_DIRECTORY.items():
            for field in required_fields:
                assert field in agency, f"Agency {code} missing field: {field}"

    def test_all_agencies_have_appeal_info(self):
        for code, agency in AGENCY_DIRECTORY.items():
            assert "appellate_authority" in agency, f"Agency {code} missing appellate_authority"
            assert "second_appeal" in agency, f"Agency {code} missing second_appeal"

    def test_fee_structure(self):
        assert FEES["central"] == 10
        # All state fees should be positive integers
        for state, fee in FEES.items():
            assert isinstance(fee, int), f"Fee for {state} is not int: {fee}"
            assert fee > 0, f"Fee for {state} is not positive: {fee}"


# ---- Integration Tests ----


class TestRTIIntegration:
    """Integration tests for the full RTI workflow."""

    def test_generate_and_track_workflow(self):
        """Test the full RTI generation -> tracking workflow."""
        generator = RTIGenerator()
        tmp_dir = tempfile.mkdtemp()
        tracker = RTITracker(db_path=os.path.join(tmp_dir, "test.db"))

        # Generate an RTI
        app = generator.awbi_inspection_request(
            facility_name="Test Farm",
            facility_location="Test Location",
            applicant_name="Test Advocate",
            applicant_address="Test Address",
        )
        text = generator.generate(app)
        assert "Test Farm" in text

        # Track the RTI
        record_id = tracker.add_rti(
            agency_code=app.agency_code,
            agency_name="Animal Welfare Board of India",
            applicant_name=app.applicant_name,
            subject=app.subject,
            questions=app.questions,
            full_text=text,
        )

        # Verify tracking
        record = tracker.get_by_id(record_id)
        assert record is not None
        assert record["status"] == "filed"
        assert record["agency_code"] == "awbi"
        assert len(record["questions"]) == 5

        # Simulate no response -> file appeal
        tracker.update_status(record_id, RTIStatus.NO_RESPONSE,
                              notes="No response received within 30 days")
        tracker.file_first_appeal(record_id, "Secretary, AWBI")

        record = tracker.get_by_id(record_id)
        assert record["status"] == "first_appeal_filed"
