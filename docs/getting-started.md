# Getting started — from zero to audit-ready in four phases

A pragmatic path for a small or mid-sized organisation, using only the files in this repository and the two companion
projects. Durations assume one part-time ISMS lead plus engaged system owners.

| Phase | Weeks | Outcome |
|-------|-------|---------|
| 1. Frame | 1–4 | Scope, policy, roles, inventory |
| 2. Assess | 5–10 | Risk assessment, impact assessments, SoA, treatment plan |
| 3. Operate | 11–26 | Controls implemented, records produced, metrics flowing |
| 4. Prove | 27–34 | Internal audit, management review, certification audit |

## Phase 1 — Frame (weeks 1–4)

1. **Decide the scope.** Start narrow (one business unit, the core platforms) — you can extend later. Write the scope statement (clause 4.3). If AI systems are in scope, list them and your organisational role (provider / user).
2. **Get leadership on paper.** Adapt `policies/information-security-policy.md` (and `policies/ai-policy.md`) and have them signed. This is clause 5 evidence.
3. **Assign roles.** Fill `templates/RACI-Matrix.xlsx` — exactly one *A* per row. Rename roles to real job titles.
4. **Inventory assets and AI systems.** Use the *Application Inventory* sheet of the [Application Risk Assessment Template](https://github.com/bizidwassim-design/application-risk-assessment-template); flag AI systems.
5. **Publish the Acceptable Use Policy** and collect acknowledgements — the quickest clause 7.3 win.

## Phase 2 — Assess (weeks 5–10)

6. **Run the risk assessment** with the Likelihood × Impact method from the template above; keep the dated report.
7. **Run AI system impact assessments** for each in-scope AI system with `templates/ai-system-impact-assessment.md`.
8. **Build the Statement of Applicability** in `templates/Statement-of-Applicability.xlsx`: mark each of the 93 (+38) controls applicable or not, justify, and record current status honestly. Expect 40–60 % "Implemented" at this stage.
9. **Write the risk treatment plan** in `templates/Risk-Treatment-Plan.xlsx`; get risk owners to sign off residual risk.
10. **Set 5–8 measurable objectives** (e.g. MFA coverage 100 %, critical patch SLA 95 %, 100 % of AI systems with a current impact assessment) — these feed the [CISO Executive Dashboard](https://github.com/bizidwassim-design/ciso-executive-dashboard).

## Phase 3 — Operate (weeks 11–26)

11. **Implement the treatment plan**, highest scores first. Adapt the remaining policies (`access-control`, `incident-management`, `supplier-security`).
12. **Start producing records** from day one: access reviews, change tickets, backup restore tests, incident records, supplier reviews. The auditor samples *records*, not intentions — see `docs/audit-evidence-list.md`.
13. **Stand up detection and response**: deploy the rules and playbooks from [soc-detection-playbooks](https://github.com/bizidwassim-design/soc-detection-playbooks); run one tabletop exercise.
14. **Measure monthly** and report quarterly to management with the dashboard.
15. **Map other frameworks** you must answer to (SOC 2, CIS, NIST CSF) with the [GRC Control Crosswalk](https://github.com/bizidwassim-design/grc-control-crosswalk) so you implement each control once.

## Phase 4 — Prove (weeks 27–34)

16. **Internal audit** by someone independent of the work audited (another team, or an external auditor). Use the two checklists in `checklists/` as the audit criteria. Record nonconformities and corrective actions.
17. **Management review** with every input required by clause 9.3 — use the agenda below.
18. **Close the gaps**, then book the certification audit (stage 1: documentation; stage 2: implementation, typically 4–8 weeks later).

### Management review agenda (clause 9.3)

1. Status of actions from previous reviews
2. Changes in external/internal issues and interested-party needs (incl. AI regulation)
3. ISMS/AIMS performance: nonconformities & corrective actions; monitoring results; audit results; objectives
4. Feedback from interested parties
5. Results of risk assessment and status of the treatment plan; AI impact assessment outcomes
6. Opportunities for continual improvement
7. **Decisions**: improvements, resource needs, changes to the ISMS/AIMS

## Common mistakes

* Writing 40 policies nobody reads instead of 6 that are enforced.
* An SoA where everything is "Implemented" — auditors test it, and it destroys credibility.
* No risk-owner sign-off on residual risk.
* Treating ISO 42001 as a separate project rather than an extension of the ISMS.
* Starting the records (reviews, tests, minutes) only a month before the audit.
