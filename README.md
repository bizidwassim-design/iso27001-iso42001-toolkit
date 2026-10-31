# ISO 27001 & ISO 42001 Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![CI](https://github.com/bizidwassim-design/iso27001-iso42001-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/bizidwassim-design/iso27001-iso42001-toolkit/actions/workflows/ci.yml) [![No macros](https://img.shields.io/badge/office%20files-no%20macros-success)](SECURITY.md) [![Fictional data](https://img.shields.io/badge/sample%20data-fictional-informational)](SECURITY.md)

A free, open-source starter kit to build an **information security management system (ISO/IEC 27001:2022)** and
extend it into an **AI management system (ISO/IEC 42001:2023)** without buying a 400-document "toolkit":
clause checklists, six policy templates, a Statement of Applicability for both Annex A sets, a risk treatment plan,
a RACI matrix, an AI system impact assessment template, the audit evidence list and a four-phase getting-started guide.

> 🇫🇷 Résumé en français en bas de page.

## Layout

```
checklists/   ISO 27001 clauses 4–10 checklist · ISO 42001 checklist (what changes for AI, Annex A families)
policies/     Information security · AI · Acceptable use · Access control · Incident management · Supplier & AI provider
templates/    Statement-of-Applicability.xlsx (ISO 27001 93 controls + ISO 42001 38 controls)
              Risk-Treatment-Plan.xlsx · RACI-Matrix.xlsx · ai-system-impact-assessment.md · CSV twins of every workbook
docs/         getting-started.md (four phases to audit) · audit-evidence-list.md (what the auditor samples)
data/         Control lists and RACI source as CSV
scripts/      build_templates.py — regenerates the workbooks from data/ with openpyxl
```

## Where to start

1. Read [docs/getting-started.md](docs/getting-started.md) — four phases, 18 steps, a management-review agenda and the mistakes to avoid.
2. Tick through [checklists/iso27001-2022-clauses-checklist.md](checklists/iso27001-2022-clauses-checklist.md) to see where you stand.
3. Open `templates/Statement-of-Applicability.xlsx` and work through the controls; the summary tab counts implemented / partial / planned / N/A automatically.
4. Adapt the policies: every bracketed value `[like this]` is a placeholder; keep the ISO references in the header — auditors love them.
5. Adding AI? Follow [checklists/iso42001-2023-checklist.md](checklists/iso42001-2023-checklist.md) and run one `ai-system-impact-assessment.md` per AI system.

## The workbooks

| File | Sheets | Built-in logic |
|------|--------|----------------|
| `Statement-of-Applicability.xlsx` | Summary · ISO 27001 Annex A · ISO 42001 Annex A | Y/N and status dropdowns, status colours, live counts and % implemented |
| `Risk-Treatment-Plan.xlsx` | Risk Treatment Plan · RTP Summary | Treatment option and status dropdowns, overdue dates in red, status counts, average inherent vs residual score; 5 fictional sample rows |
| `RACI-Matrix.xlsx` | RACI | 20 ISMS/AIMS activities × 8 roles, R/A/C/I dropdown, "exactly one A" check per row |

Every workbook has a CSV twin in `templates/` for people who do not use Excel. Regenerate after editing `data/`:

```bash
pip install openpyxl
python scripts/build_templates.py
```

Scores use the same 5×5 Likelihood × Impact bands as the
[Application Risk Assessment Template](https://github.com/bizidwassim-design/application-risk-assessment-template).
The control IDs match the [GRC Control Crosswalk](https://github.com/bizidwassim-design/grc-control-crosswalk), so you
can map each Annex A control to NIST CSF 2.0, CIS v8 and SOC 2 in one step.

## Design choices

* **Six policies, not forty.** The set covers what clause 5.2 and the most-sampled Annex A controls need; each one fits on two pages and names its ISO reference.
* **ISO 42001 as an extension.** Same clause structure, one SoA workbook with two tabs, one RACI, one incident process with AI categories.
* **Records over documents.** The evidence list tells you which *dated records* the auditor will sample so you start producing them from day one.
* **Nothing proprietary.** Control *titles* are listed for navigation; the standards' full text must be purchased from ISO or your national body. No client data; sample rows are fictional.

## Contributing

Translations, additional policy templates (e.g. cryptography, secure development), sector-specific evidence lists
and corrections are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Disclaimer

Templates and guidance, not legal advice or a guarantee of certification. Adapt to your organisation and have
them reviewed by your auditor or counsel where needed.

## License

[MIT](LICENSE).

---

## 🇫🇷 Résumé

Kit de démarrage open source pour construire un **SMSI ISO/IEC 27001:2022** et l'étendre en **système de management de
l'IA ISO/IEC 42001:2023** : check-lists des clauses 4 à 10, six modèles de politiques (sécurité de l'information, IA,
usage acceptable, contrôle d'accès, gestion des incidents, fournisseurs et fournisseurs d'IA), Déclaration d'applicabilité
pour les deux Annexes A (93 + 38 mesures), plan de traitement des risques, matrice RACI, modèle d'analyse d'impact des
systèmes d'IA, liste des preuves d'audit et guide de démarrage en quatre phases. Classeurs Excel générés par script avec
listes déroulantes et calculs automatiques, doublés en CSV. Données d'exemple fictives. Licence MIT.
