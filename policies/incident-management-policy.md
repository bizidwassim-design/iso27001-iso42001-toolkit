# Information Security & AI Incident Management Policy

| | |
|---|---|
| **Document ID** | POL-IS-004 |
| **Owner** | CISO |
| **Approved by** | [Chief Executive Officer] |
| **Version / date** | 1.0 — [YYYY-MM-DD] |
| **ISO 27001 reference** | Annex A 5.24–5.28, 6.8 · ISO 42001 A.3.3, A.8.4 |

## 1. Purpose

Ensure security events, weaknesses and AI incidents are reported, assessed, handled and learned from consistently,
and that legal notification duties (e.g. data protection authority within 72 hours) are met.

## 2. Definitions

* **Event** — an observed occurrence that may affect security (e.g. a phishing email).
* **Incident** — one or more events that compromise, or are likely to compromise, confidentiality, integrity or availability, or cause harm through an AI system (bias, unsafe output, data leakage).
* **Weakness** — a vulnerability or control gap not yet exploited.

## 3. Reporting

Anyone who suspects an event, weakness or incident reports it **immediately** to [security@yourcompany.example] /
[phone] / [ticket form]. Reporting in good faith is always protected. Suppliers must report within [24 hours] by contract.

## 4. Severity and response targets

| Severity | Examples | Acknowledge | Contain | Executive notification |
|----------|----------|-------------|---------|------------------------|
| **P1 Critical** | Ransomware, confirmed breach of Restricted data, production outage from attack, AI system causing harm at scale | 15 min | 4 h | Immediate |
| **P2 High** | Compromised account with data access, malware on a server, biased AI decision affecting customers | 1 h | 24 h | Same day |
| **P3 Medium** | Malware on a workstation (contained), lost encrypted laptop, policy violation | 4 h | 3 days | Weekly report |
| **P4 Low** | Blocked phishing, single failed control test | 1 day | 10 days | Monthly report |

## 5. Process

1. **Detect & report** — SOC alert, user report, supplier notice.
2. **Triage** — assign severity, open the incident record, name the incident lead.
3. **Contain** — isolate hosts, disable accounts, pause the AI system or fall back to manual process.
4. **Investigate** — scope, root cause, data affected, timeline; preserve evidence (see playbooks in `soc-detection-playbooks`).
5. **Eradicate & recover** — remove the cause, restore from clean backups, validate, monitor.
6. **Notify** — legal determines regulatory and contractual notifications (data subjects, authorities, customers, insurer).
7. **Learn** — post-incident review within [10 working days] for P1/P2; actions tracked in the corrective-action register.

## 6. Roles

| Role | Responsibility |
|------|----------------|
| Incident lead (SOC / CISO) | Runs the response, keeps the record, decides on escalation |
| Crisis team (CEO, CISO, CIO, Legal, Comms, HR) | Activated for P1; decisions on business impact, communication, ransom (default: no payment), notifications |
| AI system owner | Technical response for AI incidents, model rollback, affected-party communication |
| All staff | Report, preserve evidence, follow instructions, do not communicate externally |

## 7. Records and evidence

Incident records retained for [3 years]; evidence handled with chain of custody for potential legal use.

## 8. Testing

Tabletop exercise at least annually (ransomware and AI-incident scenarios), results fed into the management review.

*Template released under the MIT License by the iso27001-iso42001-toolkit project.*
