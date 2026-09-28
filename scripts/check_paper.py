"""Bounded manuscript consistency check; no mathematical proof certification."""
from pathlib import Path
from collections import Counter
import json
import re
import subprocess
import sys

assert sys.prefix != sys.base_prefix, "Use the project isolated .venv interpreter"
root = Path(__file__).resolve().parents[1]
paper = root / "paper"
# The standalone wrapper only renders the README image; it is not part of the paper.
files = [paper / "main.tex", *sorted(p for p in paper.rglob("*.tex")
                                    if p != paper / "main.tex" and not p.name.endswith("-standalone.tex"))]
text = "\n".join(p.read_text() for p in files)
labels = re.findall(r"\\label\{([^}]+)\}", text)
refs = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", text)
bib = set(re.findall(r"\\bibitem\{([^}]+)\}", text))
cites = [k.strip() for entry in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", text) for k in entry.split(",")]
errors = []
errors += [f"duplicate label: {k}" for k, n in Counter(labels).items() if n > 1]
errors += [f"missing reference: {k}" for k in set(refs) - set(labels)]
errors += [f"missing bibliography: {k}" for k in set(cites) - bib]
for rel in re.findall(r"\\input\{([^}]+)\}", text):
    if not (paper / (rel + ".tex")).is_file():
        errors.append(f"missing input: {rel}")
for marker in ["TODO", "TBD", "PLACEHOLDER", "/Users/", "rough-mobius-energy/", "PROOF-UNEXAMINED"]:
    if marker in text:
        errors.append(f"unwanted manuscript marker: {marker}")
log = (paper / "main.log").read_text(errors="replace")
for pattern in [r"^!", r"Overfull \\[hv]box", r"undefined", r"multiply defined", r"Rerun to get"]:
    if re.search(pattern, log, re.M | re.I):
        errors.append(f"TeX log issue matching {pattern}")
info = subprocess.check_output(["pdfinfo", str(paper / "main.pdf")], text=True)
pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
pdftext = subprocess.check_output(["pdftotext", str(paper / "main.pdf"), "-"], text=True)
if "??" in pdftext:
    errors.append("unresolved ?? in PDF text")
if "Jeffery Kline" not in pdftext or "Version 0.1.0" not in pdftext:
    errors.append("missing title-page identity/status")
result = {"status": "FAIL" if errors else "PASS", "pages": pages,
          "source_files": len(files), "labels": len(labels), "references": len(refs),
          "bibliography_entries": len(bib), "cited_entries": len(set(cites)),
          "python": sys.version.split()[0], "isolated": True,
          "errors": errors, "scope": "Artifact consistency only; not proof or priority certification"}
print(json.dumps(result, indent=2))
raise SystemExit(bool(errors))
