SHELL := /bin/sh
PDFLATEX ?= pdflatex
PYTHON := $(CURDIR)/.venv/bin/python
export SOURCE_DATE_EPOCH := 1790467200
export FORCE_SOURCE_DATE := 1

.PHONY: paper check readme-figure
# Four passes: a clean checkout needs them for the table of contents and
# cross-references to settle.
paper:
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex

check:
	$(PYTHON) scripts/check_paper.py

readme-figure:
	cd paper/figures && $(PDFLATEX) -interaction=nonstopmode -halt-on-error redheffer-comparison-standalone.tex
	cd paper/figures && pdftoppm -r 220 -png -singlefile redheffer-comparison-standalone.pdf redheffer-comparison
