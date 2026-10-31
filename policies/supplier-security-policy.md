# Supplier & AI Provider Security Policy

| | |
|---|---|
| **Document ID** | POL-IS-005 |
| **Owner** | CISO (with Procurement) |
| **Approved by** | [Chief Operating Officer] |
| **Version / date** | 1.0 — [YYYY-MM-DD] |
| **ISO 27001 reference** | Annex A 5.19–5.23 · ISO 42001 A.10 · NIST CSF 2.0 GV.SC |

## 1. Purpose

Manage information security and AI risks arising from suppliers, cloud services and AI providers throughout the
relationship: selection, contracting, monitoring and exit.

## 2. Tiering

| Tier | Criteria | Due diligence | Review |
|------|----------|---------------|--------|
| **1 Critical** | Processes Restricted/Confidential data, or supports a critical business process, or provides an AI model used in decisions about people | Questionnaire + evidence (ISO 27001 / SOC 2 report, pen-test summary), architecture review, legal review | Annual + on incident |
| **2 Important** | Processes Internal data or supports important processes | Questionnaire + certificate check | Every 2 years |
| **3 Standard** | No company data, or Public data only | Self-attestation at onboarding | On renewal |

## 3. Requirements before contract

* Tier assigned by Procurement with the CISO; due diligence completed and risks recorded in the risk register.
* Data protection assessment where personal data is processed; data location and sub-processors known.
* For **AI providers**: documentation of intended use, limitations, training-data sources, evaluation results, security testing, and whether customer data is used for training (must be opt-out).

## 4. Contract clauses (minimum)

1. Confidentiality and data-processing terms.
2. Security controls aligned with this policy; right to audit or to receive assurance reports.
3. Incident notification within [24 hours] of discovery.
4. Vulnerability management and patching commitments.
5. Sub-processor approval and flow-down of obligations.
6. Business continuity commitments and RTO/RPO.
7. Return or deletion of data at exit, with certificate; **exit plan and data export format** for Tier 1.
8. For AI providers: responsibility allocation for impact assessment, monitoring, incident handling and user information.

## 5. During the relationship

* Service and security performance reviewed at the frequency in §2; findings tracked to closure.
* Supplier access to systems follows the Access Control Policy (named accounts, MFA, expiry).
* Changes to services, locations or sub-processors are assessed before acceptance.

## 6. Exit

Access revoked, data returned/deleted, certificates obtained, contract register updated.

## 7. Records

Supplier register with tier, owner, due-diligence date, contract clauses status, next review.

*Template released under the MIT License by the iso27001-iso42001-toolkit project.*
