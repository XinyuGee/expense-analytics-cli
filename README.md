# Expense Analytics CLI

A small Python command-line project demonstrating version control workflows, AI-assisted code review, conflict resolution, Conventional Commits, testing, and CI/CD.

## Project Overview
This project reads as a final-project-style repository for SYSEN 5493. It focuses on showing disciplined Git usage and AI collaboration practices, not just producing code.

## Features
- command-line entry point in `main.py`
- utility analytics functions in `utils.py`
- mean calculation
- standard deviation calculation
- median calculation
- explicit error handling for empty input in selected functions
- unit tests with `pytest`
- GitHub Actions CI pipeline for linting and tests

## Repository Highlights
This repo demonstrates:
- feature branching
- PR-style documentation
- AI-assisted code review notes
- merge conflict creation and resolution
- Conventional Commit messages
- automated CI workflow

## Files
- `main.py` — simple CLI entry point
- `utils.py` — analytics helper functions
- `AI_CODE_REVIEW.md` — notes on AI-catchable vs human-judgment review issues
- `PR_DESCRIPTION.md` — PR-style summary for the utility feature
- `tests/test_utils.py` — unit tests
- `.github/workflows/ci.yml` — CI pipeline

## Setup
Clone the repository:

```bash
git clone git@github.com:XinyuGee/expense-analytics-cli.git
cd expense-analytics-cli
