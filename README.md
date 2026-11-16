# Horizon Retail — AI Opportunity & Strategy Analysis

**Python | Pandas | Jupyter | Matplotlib | Seaborn | Pytest**

A reproducible, evidence-led **business decision-analysis** portfolio based on a fictional Horizon Retail case from a previously submitted CAIBL AI3120 P101 assessment. **Not** a deployed AI solution or a predictive ML model.

## Business decision
Compare four AI opportunities using a five-criterion weighted matrix. The original recommendation is a **conditional, human-supervised customer enquiry drafting pilot** (3.80/5). Inventory forecasting ranks second (3.60/5). If customer enquiry data readiness drops from 3 to 1, customer enquiry falls to 3.40/5 and inventory becomes first.

## What this repository demonstrates
- Reproducible weighted scoring, ranking and scenario testing in modular Python
- Transparent source-data register, assumptions, sensitivity and risk interpretation
- Publication-quality analytical charts and business tables
- Input validation and automated tests
- Proposed 90-day pilot governance, budget and KPI definitions

## Quick start (Windows PowerShell)
```powershell
cd "C:\Rakesh Project\Horizon-Retail-AI-Opportunity-Strategy"
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m jupyter notebook
```
Open `notebooks/Horizon_Retail_AI_Opportunity_Strategy.ipynb`, select the `.venv` Python kernel, then **Run All**. Run from the repository root or use the notebook's automatic path resolution.

## Files
- `notebooks/` — complete notebook, markdown explanations, tables and charts
- `data/case_inputs/` — fictional case facts and submitted scoring inputs
- `src/scoring.py` — reusable and validated calculations
- `tests/` — deterministic scoring and sensitivity tests
- `visualizations/` — generated PNG charts after executing the notebook
- `reports/` — generated CSV tables after executing the notebook
- `documentation/` — evidence, assumptions and methodology

## Scope and limitations
All input figures are fictional case information. Scoring and budgets are planning judgments, not measured business outcomes. No customer-level records, model training, deployment, or realized pilot benefits are claimed. The original assessment submission remains unchanged and is not republished.

## Portfolio positioning
This project demonstrates Python analytical programming, reproducibility, validation and decision communication. Separate backend/API projects should demonstrate REST APIs and database engineering.

## Learning-focused walkthrough
The notebook includes a beginner-to-intermediate narrative: understand the case, organize inputs, implement scoring, visualize findings, challenge the ranking, verify the logic and explain limitations. It does not pretend to be a deployed enterprise AI solution.

## Software and tools actually used
Python, Jupyter, Pandas, NumPy, Matplotlib, Seaborn, Pytest and Windows PowerShell. Excel was the source assessment calculation reference. Git/GitHub publication is pending local verification. No MySQL, FastAPI, Power BI or Tableau components are claimed.

## Verification, interviews and CV
- `documentation/LOCAL_VERIFICATION.md`: check off real Windows tests and record genuine issues
- `documentation/INTERVIEW_PREPARATION.md`: explain design choices and limitations in interviews
- `documentation/CV_ENTRY_DRAFT.md`: accurate project wording after local verification

## AI assistance disclosure
AI assistance was used in preparing and refining the portfolio code, narrative and documentation. Inputs, calculations, and claims must be reviewed by the repository owner before publication.
