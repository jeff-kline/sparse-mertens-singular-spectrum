# Verification record — version 0.1.0 candidate

Recorded 2026-09-27.

## What is verified here

This record covers artifact consistency and reproducibility: the document
builds deterministically, its labels, citations and log are clean, and every
tracked file matches the manifest. It does not verify proofs. The proof audits,
source comparisons, and their dispositions are in `audit/LEDGER.md` and
`audit/reports/`.

No theorem in the paper rests on a numerical computation. The two proof
auditors ran small exact and floating-point falsification checks (recorded in
their reports). Those checks are not part of the release evidence and are not
reproduced here.

## Environment

| Tool | Version |
|---|---|
| pdfTeX | 3.141592653-2.6-1.40.22 (TeX Live 2021, MacPorts 2021.58693_2) |
| Python (checker, isolated `.venv`) | 3.12.14; standard library only |
| Poppler `pdfinfo` / `pdftotext` | 26.07.0 |
| OS | macOS (Darwin 25.6.0) |

The Makefile fixes `SOURCE_DATE_EPOCH=1790467200` (2026-09-27 00:00 UTC) and
`FORCE_SOURCE_DATE=1`, so the PDF creation date and identifiers are fixed.

## Commands and outputs

```sh
python3 -m venv .venv
make paper    # two pdfLaTeX passes
make paper    # repeated; output unchanged
make check
shasum -a 256 paper/main.pdf
shasum -a 256 -c MANIFEST.sha256
```

`make check` output:

```json
{
  "status": "PASS",
  "pages": 39,
  "source_files": 11,
  "labels": 121,
  "bibliography_entries": 18,
  "cited_entries": 18,
  "python": "3.12.14",
  "isolated": true,
  "errors": [],
  "scope": "Artifact consistency only; not proof or priority certification"
}
```

The checker fails on duplicate or missing labels, missing bibliography keys,
missing inputs, placeholder markers, TeX errors, overfull boxes, undefined or
multiply defined references, rerun warnings, unresolved `??` in the PDF text,
and a missing title-page author or version line.

Reading copy:

```text
paper/main.pdf  39 pages
SHA-256 bf477dddf4d5d65ad5f26be42f2de4c4e37dda3dabe20b5f5a34152fb420b915
```

Two consecutive builds from the same source produced this identical hash. A
different TeX distribution may produce a different but equivalent PDF.

## Visual inspection

All 39 pages were rendered and inspected: the title block is centered, the
n = 120 comparison figure is intact, and no text runs into the margin.

## Excluded material

Not part of this repository: the local Python environment, temporary
renderings, copies of third-party papers consulted during the literature
comparison, and the exploratory research notes from the same period.
