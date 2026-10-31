# Artificial Intelligence Policy

| | |
|---|---|
| **Document ID** | POL-AI-001 |
| **Owner** | AI Governance Lead |
| **Approved by** | [Chief Executive Officer] |
| **Version / date** | 1.0 — [YYYY-MM-DD] |
| **Review cycle** | Annual, or on change in AI regulation or a significant AI incident |
| **ISO 42001 reference** | Clause 5.2, Annex A 2.2–2.4, A.9 |

## 1. Purpose

Defines how [Organisation] develops, procures and uses artificial intelligence (AI) systems responsibly, in line with its
values, applicable law and the AI management system (AIMS).

## 2. Scope

All AI systems developed, purchased, integrated or used by [Organisation], including generative-AI assistants used by
staff, machine-learning models embedded in products, and AI features of third-party services. The AI system inventory
[INV-AI-001] lists in-scope systems and their owners.

## 3. Principles

| Principle | What it means at [Organisation] |
|-----------|---------------------------------|
| **Accountability** | Every AI system has a named owner; decisions with significant effect on people keep a human accountable |
| **Fairness** | Systems are tested for bias before release and monitored in operation |
| **Transparency** | People are told when they interact with AI or are subject to AI-assisted decisions; explanations are available on request |
| **Safety & security** | AI systems inherit the information security policy; AI-specific threats (prompt injection, data poisoning, model theft) are assessed |
| **Privacy** | Personal data in training, prompts and outputs is handled under the data protection policy; no personal or confidential data in public AI tools |
| **Reliability** | Performance is validated against defined criteria and monitored for drift |
| **Human oversight** | Humans can intervene, override and switch off |

## 4. Policy statements

1. An **AI system impact assessment** (`templates/ai-system-impact-assessment.md`) is completed and approved before a new AI system is deployed or an existing one is significantly changed.
2. AI systems are classified by risk; high-risk uses (decisions about employment, credit, health, safety, legal rights) require legal review and enhanced controls.
3. Only **approved AI tools** listed in [INV-AI-001] may be used with internal, confidential or personal data. Public tools may be used with public information only.
4. AI-generated content used externally is reviewed by a competent person and labelled where required.
5. Training and evaluation data have documented provenance, quality criteria and lawful basis.
6. AI systems log events sufficient to investigate incidents and explain outcomes.
7. Suppliers of AI systems or models provide documentation on intended use, limitations, data and testing; contracts allocate responsibilities.
8. AI incidents, near-misses and concerns are reported through the incident process; retaliation for raising concerns is prohibited.
9. Staff developing or using AI receive role-appropriate training.

## 5. Roles and responsibilities

| Role | Responsibility |
|------|----------------|
| Top management | Approve the policy, allocate resources, review AIMS performance |
| AI Governance Lead | Own the AIMS, inventory, impact-assessment process, reporting |
| AI system owners | Impact assessment, requirements, validation, monitoring of their system |
| Data & AI teams | Build and operate systems under the life-cycle controls |
| Legal & compliance | Regulatory mapping (e.g. EU AI Act), contracts, high-risk reviews |
| All personnel | Use only approved tools, follow the acceptable-use rules, report concerns |

## 6. Related documents

Information Security Policy (POL-IS-001) · Acceptable Use Policy (POL-IS-002) · AI system inventory · AI system impact
assessment template · Data protection policy · Supplier Security Policy (POL-IS-005)

## 7. Approval

| Name | Role | Signature | Date |
|------|------|-----------|------|
| | Chief Executive Officer | | |
| | AI Governance Lead | | |

*Template released under the MIT License by the iso27001-iso42001-toolkit project. Adapt before use; this is not legal advice.*
