# AI-Bug-Triage

AI-powered QA tool that analyzes bug reports and generates test cases and regression test scenarios.

## Features

* Upload bugs using Excel/CSV
* Analyze bug severity
* Identify bug priority
* Identify affected component
* Detect duplicate bugs
* Generate test cases
* Generate regression test scenarios
* Streamlit dashboard

## Workflow

```text
Bug Report
    ↓
Excel / CSV
    ↓
Bug Analysis
    ↓
Duplicate Detection
    ↓
Test Case Generation
    ↓
Regression Test Generation
```

## Tech Stack

* Python
* Streamlit
* Pandas
* Scikit-learn
* OpenPyXL
* Pytest

## Run

```bash
git clone https://github.com/kamilath/AI-Bug-Triage.git
cd AI-Bug-Triage

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

## Testing

```bash
pytest
```

## Purpose

This project helps QA engineers automate **bug analysis, duplicate detection, test case generation, and regression test generation** from bug reports.
