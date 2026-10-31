# AI System Impact Assessment (ISO/IEC 42001 §6.1.4, Annex A.5)

| | |
|---|---|
| **Assessment ID** | AIA-[000] |
| **AI system** | [Name, version] |
| **System owner** | [Name, role] |
| **Assessor(s)** | [Names] |
| **Date / status** | [YYYY-MM-DD] · Draft / Approved |
| **Trigger** | New system / significant change / periodic review |

## 1. System description

| Question | Answer |
|----------|--------|
| What does the system do, and what decision or output does it produce? | |
| Intended use and users | |
| Explicitly **not** intended uses | |
| Type of model (rule-based, ML, LLM, third-party API) and provider | |
| Data used: training, fine-tuning, prompts, retrieval sources | |
| Degree of automation: informs a human / recommends / decides automatically | |
| Where it sits in the business process (diagram reference) | |

## 2. Affected parties

| Party | How they are affected | Vulnerable groups? |
|-------|-----------------------|--------------------|
| Users (staff) | | |
| Customers / individuals subject to outputs | | |
| Society / environment | | |
| Organisation (legal, financial, reputational) | | |

## 3. Impact analysis

Score Likelihood (1–5) × Severity (1–5) = Score; bands Low 1–4, Medium 5–9, High 10–16, Critical 17–25.

| # | Potential impact | Example scenario | L | S | Score | Existing controls |
|---|------------------|------------------|---|---|-------|-------------------|
| 1 | Unfair or discriminatory outcome | | | | | |
| 2 | Inaccurate / unreliable output acted upon | | | | | |
| 3 | Lack of transparency or explainability | | | | | |
| 4 | Privacy — personal data in training, prompts or outputs | | | | | |
| 5 | Security — prompt injection, data leakage, model theft, poisoning | | | | | |
| 6 | Safety or physical harm | | | | | |
| 7 | Loss of human oversight / over-reliance | | | | | |
| 8 | Legal / regulatory non-compliance (e.g. EU AI Act category) | | | | | |
| 9 | Environmental (compute) | | | | | |
| 10 | Societal (misinformation, manipulation, job displacement) | | | | | |

## 4. Regulatory classification

| Framework | Classification | Rationale |
|-----------|----------------|-----------|
| EU AI Act (if applicable) | Prohibited / High-risk / Limited (transparency) / Minimal | |
| Data protection (DPIA required?) | Yes / No | |
| Sector rules | | |

## 5. Treatment and residual impact

| # | Action | Owner | Due | Residual score |
|---|--------|-------|-----|----------------|
| | | | | |

Human oversight mechanism: [who can intervene, how, within what time]
Transparency measures: [user notice, explanation, labelling]
Monitoring plan: [metrics, frequency, thresholds, drift]
Fallback / kill switch: [manual process, rollback]

## 6. Conclusion

☐ Proceed · ☐ Proceed with conditions (listed above) · ☐ Do not proceed / redesign

| Role | Name | Decision | Date |
|------|------|----------|------|
| System owner | | | |
| AI Governance Lead | | | |
| Legal & compliance (high-risk only) | | | |

Next review date: [YYYY-MM-DD] or on significant change.

*Template released under the MIT License by the iso27001-iso42001-toolkit project. Not legal advice.*
