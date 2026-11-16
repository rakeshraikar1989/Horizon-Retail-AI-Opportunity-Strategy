$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (-not (Test-Path '.venv\Scripts\python.exe')) { py -m venv .venv }
& '.\.venv\Scripts\python.exe' -m pip install -r requirements.txt
& '.\.venv\Scripts\python.exe' -m pytest -q
& '.\.venv\Scripts\python.exe' -m jupyter nbconvert --to notebook --execute 'notebooks\Horizon_Retail_AI_Opportunity_Strategy.ipynb' --output 'Horizon_Retail_AI_Opportunity_Strategy.ipynb' --output-dir 'notebooks' --ExecutePreprocessor.timeout=600
Write-Host 'Notebook execution and tests completed.'
