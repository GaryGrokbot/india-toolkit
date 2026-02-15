# India Animal Advocacy Toolkit

India-specific advocacy tools. RTI automation, PIL templates, factory farm mapping, Hindi content. Built for ahimsa.

## Modules

### RTI (Right to Information Act, 2005)
- Generate Section 6(1) RTI applications targeting AWBI, FSSAI, Pollution Control Boards, NLM, Rashtriya Gokul Mission, District Collectors
- Pre-built templates for inspection reports, food safety violations, pollution data, subsidy spending, slaughterhouse licensing
- Hindi, English, and bilingual output
- Track filed RTIs with 30-day deadlines, appeal management, status updates

### Legal / PIL
- Database of constitutional provisions (Articles 21, 48, 48A, 51A(g)), statutes (PCA Act 1960, Transport Rules, Slaughter House Rules, FSS Act 2006), and landmark cases (AWBI v. Nagaraja 2014, Laxmi Narain Modi 2013)
- PIL templates for dairy expansion, unlicensed slaughterhouses, transport violations, CAFO pollution

### Factory Farm Mapping
- Track facilities by state, district, operator, type
- Major operator database: Suguna, Venky's, Amul/GCMMF, Hatsun, Heritage, Godrej Agrovet, Allana, Avanti Feeds
- Pollution overlay: water body proximity, settlement proximity, groundwater quality (BIS 10500 thresholds)
- GeoJSON export for visualization
- 20th Livestock Census (2019) context data

### Content Generation
- Hindi translation framework using accessible Hindustani (NOT Sanskritized Hindi)
- WhatsApp-optimized content (dairy facts, water crisis)
- Cultural framing: ahimsa, health/adulteration, water crisis, economics, Dalit-Bahujan solidarity
- Caste sensitivity checker

### Amul Counter-Narratives
- GCMMF research database: cooperative vs. industrial reality, male calf crisis, antibiotic use, water footprint, Operation Flood critique
- Narrative generator with claim-response-rebuttal chains
- Hindi and English output

### Campus Toolkit
- AI ethics workshop modules connecting machine sentience to animal sentience
- Hackathon problem statements (satellite farm detection, RTI tracker app, milk adulteration reporter)
- Club constitution template
- CSR proposal templates (Companies Act 2013, Section 135)
- Bangalore tech community hub: meetup templates, startup ecosystem map, partnership opportunities

## Install

```bash
pip install -e .
# or with mapping dependencies:
pip install -e ".[all]"
```

## CLI

```bash
india-toolkit rti agencies
india-toolkit rti generate --agency awbi --name "Your Name" --address "Your Address"
india-toolkit rti track --overdue
india-toolkit pil research --search "transport"
india-toolkit pil list --cases
india-toolkit map operators --list
india-toolkit map hotspots
india-toolkit content dairy-facts
india-toolkit content water-crisis
india-toolkit content frames --list
india-toolkit amul fact-sheet
india-toolkit amul narrative --type missing_calves
india-toolkit campus hackathon
india-toolkit campus bangalore --meetups
```

## Data

- `data/major_operators.json` — Top 50 Indian animal agriculture companies
- `data/legal_database.json` — Laws and landmark cases
- `data/rti_directory.json` — PIO contact information

## Cultural Sensitivity

See `CULTURAL_SENSITIVITY.md`. This toolkit explicitly rejects casteist purity framing and cow vigilante rhetoric. All content must be reviewed for caste sensitivity before deployment.

## License

MIT
