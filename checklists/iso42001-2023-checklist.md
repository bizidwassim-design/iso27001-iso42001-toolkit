# ISO/IEC 42001:2023 — AI management system checklist

ISO 42001 uses the same Harmonised Structure as ISO 27001 (clauses 4–10), so an organisation with an ISMS can
**extend** it rather than build a second system. The table flags what is new or different for AI. Annex A controls
(38) are listed in `templates/statement-of-applicability-iso42001.csv`.

Status legend: ☐ not started · ◐ in progress · ☑ done

## Clauses 4–10 — what changes compared with ISO 27001

| # | Requirement | AI-specific points | Status | Evidence |
|---|-------------|--------------------|--------|----------|
| 4.1 | Context of the organisation | Determine the organisation's **role(s)**: AI provider, producer, user, partner, subject, relevant authority. Consider climate change as an issue (2024 amendment). | ☐ | Context & roles statement |
| 4.2 | Interested parties | Include affected individuals and society, regulators (e.g. EU AI Act), customers of AI-enabled products | ☐ | Interested-parties register |
| 4.3 | Scope of the AIMS | Which AI systems, which life-cycle stages, which roles | ☐ | AIMS scope statement + AI system inventory |
| 4.4 | AI management system | Established, maintained, improved | ☐ | AIMS manual |
| 5.2 | AI policy | Covers responsible development/use, alignment with values, principles (fairness, transparency, accountability, safety, privacy, security) | ☐ | `policies/ai-policy.md` |
| 5.3 | Roles | AI governance lead, system owners, impact-assessment approvers | ☐ | RACI matrix |
| 6.1.2 | AI risk assessment | Risk criteria include impacts on **individuals, groups and society**, not only the organisation | ☐ | AI risk methodology |
| 6.1.3 | AI risk treatment | Controls compared with Annex A; **Statement of Applicability**; treatment plan | ☐ | SoA (ISO 42001 tab), treatment plan |
| 6.1.4 | **AI system impact assessment** *(unique to 42001)* | Process to assess consequences for individuals and society for each AI system, documented, results used in risk treatment and communicated | ☐ | `templates/ai-system-impact-assessment.md` per system |
| 6.2 | AI objectives | Measurable, e.g. % of AI systems with a current impact assessment | ☐ | Objectives sheet |
| 7.2 | Competence | Data science, AI ethics, domain expertise | ☐ | Competence matrix |
| 7.4 | Communication | Transparency to users and affected parties about AI use | ☐ | Communication plan, user notices |
| 8.2–8.4 | Operation | AI risk assessment, treatment **and impact assessment** carried out at planned intervals and on significant change | ☐ | Dated records |
| 9.1 | Monitoring | Model performance, drift, incidents, complaints | ☐ | AI metrics report |
| 9.2 | Internal audit | Audit AI life-cycle controls, not only policies | ☐ | Audit reports |
| 9.3 | Management review | Inputs include impact-assessment outcomes and changes in AI regulation | ☐ | Minutes |
| 10 | Improvement | Nonconformities incl. AI incidents and near-misses | ☐ | Corrective action register |

## Annex A — control families (38 controls)

| Family | Controls | Minimum evidence |
|--------|----------|------------------|
| A.2 Policies | 3 | AI policy, alignment statement, review record |
| A.3 Internal organisation | 2 | Roles, concern-reporting channel |
| A.4 Resources | 5 | Resource documentation: data, tooling, compute, people |
| A.5 Impact assessment | 4 | Process + one completed assessment per in-scope AI system |
| A.6 AI system life cycle | 9 | Objectives, design docs, verification & validation records, deployment plan, monitoring, event logs |
| A.7 Data for AI systems | 5 | Data provenance, quality criteria, preparation records |
| A.8 Information for interested parties | 4 | User documentation, incident communication, external reporting |
| A.9 Use of AI systems | 3 | Responsible-use process, intended-use statement |
| A.10 Third-party and customer relationships | 3 | Supplier requirements, customer responsibilities |

## Integration tips (ISMS → AIMS)

1. Add AI systems to the existing asset inventory with an "AI system" flag; reuse the same risk scales.
2. Extend the SoA workbook with the ISO 42001 tab instead of starting a new document.
3. Reuse the incident process; add AI-specific categories (bias, drift, hallucination with impact, prompt injection, data leakage).
4. One management review, two agendas: ISMS items then AIMS items.
5. Map the overlap with `grc-control-crosswalk` (ISO 27001 ↔ ISO 42001 column) to avoid duplicating controls.
