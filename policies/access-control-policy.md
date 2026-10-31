# Access Control Policy

| | |
|---|---|
| **Document ID** | POL-IS-003 |
| **Owner** | CISO |
| **Approved by** | [Chief Information Officer] |
| **Version / date** | 1.0 — [YYYY-MM-DD] |
| **ISO 27001 reference** | Annex A 5.15–5.18, 8.2–8.5 · CIS v8 5, 6 · NIST CSF 2.0 PR.AA |

## 1. Principles

**Need to know · least privilege · segregation of duties · unique identity · default deny.**

## 2. Identity life cycle

| Step | Rule | Timing |
|------|------|--------|
| Joiner | Account created from an HR-approved request; standard role profile; MFA enrolled before first use | Day 1 |
| Mover | Rights re-assessed by the new manager; old rights removed | Within 5 working days |
| Leaver | All access disabled on the HR termination date; tokens and sessions revoked; devices returned | Same day |
| Contractor / third party | Sponsor named; expiry date set at creation (max 12 months); renewed only on request | At creation |

## 3. Authentication

* Passwords: minimum [14] characters, no reuse of the last [10], blocked against breached-password lists; no forced periodic change unless compromised.
* **MFA is mandatory** for all remote access, cloud services, email and any privileged or administrative access.
* Shared and generic accounts are prohibited unless documented, owned and technically unavoidable.
* Service accounts: non-interactive, least privilege, credentials in the secrets vault, rotated at least annually.

## 4. Privileged access

* Administrative rights are granted to separate admin accounts, not the user's daily account.
* Privileged access uses just-in-time elevation or a privileged-access management tool where available; sessions are logged.
* Local administrator rights on workstations are removed by default; exceptions expire after [90] days.
* Privileged accounts are reviewed **monthly**.

## 5. Authorisation and reviews

* Access to Confidential/Restricted information requires approval by the information owner.
* Managers review their teams' access **quarterly**; owners of critical systems certify user lists **quarterly**; evidence retained.
* Segregation of duties is enforced for payments, code deployment to production and user administration.

## 6. Remote and network access

* Remote access only through the approved zero-trust / VPN service with device compliance checks.
* Network access control on wired and wireless networks; guest networks are isolated.

## 7. Logging

Authentication events, privilege use and access changes are logged centrally and retained for at least [12] months.

## 8. Exceptions

Documented, approved by CISO and the system owner, with compensating controls and an expiry date.

*Template released under the MIT License by the iso27001-iso42001-toolkit project.*
