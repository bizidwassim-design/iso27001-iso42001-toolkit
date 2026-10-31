# Contributing

Welcome contributions:

* **Translations** of checklists, policies and guides (add a language suffix: `ai-policy.fr.md`).
* **New policy templates** that map to Annex A controls not yet covered (cryptography, secure development, logging, physical security, business continuity).
* **Evidence lists** for specific sectors or regulators.
* **Corrections** to clause or control references.

## Ground rules

1. Keep every template short (two pages), with the document-control header and the ISO reference line.
2. Do not reproduce the text of the standards — list clause/control *titles* and your own wording only. The standards are copyrighted by ISO.
3. Sample content must be **fictional**; never include real company names, data or incident details.
4. Workbooks are generated: change `data/*.csv` or `scripts/build_templates.py`, run the script, and commit both the source and the generated files.
5. Run a quick open/recalculate in Excel or LibreOffice before submitting a workbook change.

## Process

Open an issue to discuss anything larger than a typo fix, then a pull request describing what changed and why.
By contributing you agree your work is released under the [MIT License](LICENSE) and you accept the
[Code of Conduct](CODE_OF_CONDUCT.md).
