# Audit evidence list — what the certification auditor will ask for

Prepare these **before** the stage 1 audit. "Record" means a dated artefact that proves the activity happened, not
the procedure that says it should. Where ISO 42001 is in scope, the AI column adds what the AIMS auditor needs.

## A. Management system (clauses 4–10)

| # | Evidence | ISO 27001 | ISO 42001 addition | Ready? |
|---|----------|-----------|--------------------|--------|
| 1 | Scope statement with boundaries, locations, interfaces | 4.3 | AI systems and life-cycle stages in scope; organisational role(s) | ☐ |
| 2 | Context analysis and interested-parties register | 4.1, 4.2 | Affected individuals, society, regulators | ☐ |
| 3 | Signed information security policy; communication evidence | 5.2 | Signed AI policy | ☐ |
| 4 | Roles & responsibilities (RACI, org chart, job descriptions) | 5.3 | AI governance roles | ☐ |
| 5 | Risk assessment methodology and risk acceptance criteria | 6.1.2 | Criteria covering impacts on individuals and society | ☐ |
| 6 | Latest risk assessment report (dated) and risk register | 6.1.2, 8.2 | AI risk register entries | ☐ |
| 7 | **Risk treatment plan** with owners, dates, progress, risk-owner approval | 6.1.3, 8.3 | — | ☐ |
| 8 | **Statement of Applicability**, every control justified | 6.1.3 d) | ISO 42001 Annex A SoA | ☐ |
| 9 | AI system impact assessments for each in-scope system | — | 6.1.4, A.5 | ☐ |
| 10 | Security objectives with measurements and progress | 6.2 | AI objectives | ☐ |
| 11 | ISMS change records | 6.3 | — | ☐ |
| 12 | Competence matrix, training records, certificates | 7.2 | AI/data-science competence | ☐ |
| 13 | Awareness programme evidence (campaigns, attendance, quiz results) | 7.3 | AI acceptable-use awareness | ☐ |
| 14 | Communication plan | 7.4 | Transparency to users / affected parties | ☐ |
| 15 | Document register with versions, approvals, review dates | 7.5 | — | ☐ |
| 16 | Operational procedures and records (see B) | 8.1 | AI life-cycle records (see C) | ☐ |
| 17 | Monitoring & measurement results (KPI reports, dashboard) | 9.1 | Model performance / drift reports | ☐ |
| 18 | Internal audit programme, audit plan, **audit reports**, auditor independence | 9.2 | AIMS audit coverage | ☐ |
| 19 | **Management review minutes** covering all required inputs and outputs | 9.3 | AI inputs (impact assessments, regulation changes) | ☐ |
| 20 | Nonconformity & corrective-action register with effectiveness checks | 10.2 | AI incidents / near-misses | ☐ |

## B. Annex A control records — the ones most often sampled

| Control area | Records sampled |
|--------------|-----------------|
| A.5.9 Asset inventory | Inventory export with owners, classification; reconciliation against discovery tool |
| A.5.15–5.18 Access control | Joiner/mover/leaver tickets; quarterly access review sign-offs; privileged account list |
| A.5.19–5.22 Suppliers | Supplier register with tiers; due-diligence questionnaires; contracts with security clauses; review minutes |
| A.5.24–5.28 Incidents | Incident records for the period; post-incident reviews; tabletop exercise report |
| A.5.29–5.30 Continuity | BIA, continuity plans, **test results** |
| A.5.31–5.36 Compliance | Legal register; data-protection records; policy compliance checks |
| A.6.1–6.8 People | Screening records; signed NDAs/AUP; onboarding/offboarding checklists; disciplinary process |
| A.7 Physical | Visitor logs; access-badge reviews; clean-desk spot checks |
| A.8.7 Malware / A.8.8 Vulnerabilities | EDR coverage report; vulnerability scan reports; **patch SLA metrics**; pen-test report and remediation tracking |
| A.8.9 Configuration | Baselines; configuration drift reports |
| A.8.13 Backup | Backup schedule; **restore test records** |
| A.8.15–8.16 Logging & monitoring | Log retention settings; SIEM alert samples with triage notes (see `soc-detection-playbooks`) |
| A.8.24 Cryptography | Key inventory; certificate expiry monitoring |
| A.8.25–8.29 Secure development | SDLC policy; code review and security testing records; separation of environments |
| A.8.32 Change management | Change tickets with approval and test evidence |

## C. ISO 42001 Annex A records

| Control area | Records sampled |
|--------------|-----------------|
| A.4 Resources | Data, tooling, compute and human-resource documentation per AI system |
| A.5 Impact assessment | Completed and approved assessments; evidence results fed into treatment |
| A.6.2 Life cycle | Requirements/specification; design docs; **verification & validation results**; deployment approval; monitoring reports; event logs |
| A.7 Data | Data provenance records; quality criteria and checks; preparation records |
| A.8 Interested parties | User documentation; incident communications; external reports |
| A.9 Use | Responsible-use process; intended-use statements |
| A.10 Third parties | AI supplier assessments; contracts allocating responsibilities; customer information |

## Tips

* Auditors sample: have the **list** of records (e.g. all changes this quarter) ready, then be able to open any one.
* A record without a date, author or approval is not evidence.
* Keep the evidence index in one place (`templates/statement-of-applicability-*.csv` has an *Evidence location* column for this).
