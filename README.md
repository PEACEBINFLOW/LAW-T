# LAW-T: A Time-Labeled Self-Evolving Programming System

[![Build Status](https://github.com/PEACEBINFLOW/LAW-T/actions/workflows/test.yml/badge.svg)](https://github.com/PEACEBINFLOW/LAW-T/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Status](https://img.shields.io/badge/status-prototype-orange)

> A temporal programming framework where code evolves lawfully through time-labeled computation and self-governing syntax.
# LAW-T: A Time-Labeled Self-Evolving Programming System

**Author:** Peace Thabiwa (SageWorks AI)  
**Status:** Thesis + Prototype skeleton

This repository contains:
- A formal thesis (`docs/thesis.md`) describing LAW-T.
- A minimal Python prototype for **TLB minting** and a **content-addressed ledger**.
- Example â€œlawsâ€ encoded as YAML with proofs placeholders.
- Docs scaffold and GitHub workflows to invite contributions.

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Mint a TLB and store a sample law in the ledger
python src/main.py law add examples/laws/for_each.law.yaml

# Show ledger contents
python src/main.py ledger list
```

## Repo Layout

```
LAW-T/
â”œâ”€ src/lawt/
â”‚  â”œâ”€ __init__.py
â”‚  â”œâ”€ tlb.py            # Time-Labeled Binary minting (HLC-based)
â”‚  â”œâ”€ ledger.py         # Content-addressed store with metadata
â”‚  â”œâ”€ law_registry.py   # Simple law loader/validator stub
â”‚  â””â”€ cli.py            # CLI commands used by src/main.py
â”œâ”€ src/main.py
â”œâ”€ examples/laws/for_each.law.yaml
â”œâ”€ docs/thesis.md
â”œâ”€ docs/overview.md
â”œâ”€ docs/roadmap.md
â”œâ”€ LICENSE (MIT)
â”œâ”€ requirements.txt
â”œâ”€ .gitignore
â”œâ”€ .github/workflows/test.yml
â””â”€ CITATION.cff
```

> **Note:** The Python code is a **minimal educational scaffold** to demo core ideas (TLB, ledger, law files). It is *not* a full LAW-T runtime.

## Contributing

See `CONTRIBUTING.md` and open issues/PRs. Focus areas: richer SIR model, effect masks, meta-law proofs, and HLC edge-cases.
