@echo off
:: 1. Navigate to your project directory dynamically
cd /d "%~dp0"

:: 2. Activate your project's virtual environment
call .venv\Scripts\activate
:: 3. Run your active pytest command
pytest -s -v -m "regression" --html=reports/automation_report.html --self-contained-html --browser="chrome"

REM pytest -s -v -m "sanity" --html=reports/automation_report.html --self-contained-html --browser="chrome"
REM pytest -s -v -m "regression" --html=reports/automation_report.html --self-contained-html --browser="edge"
REM pytest -s -v -m "sanity" --html=reports/automation_report.html --self-contained-html --browser="edge"
REM pytest -s -v -m "regression" --html=reports/automation_report.html --self-contained-html --browser="firefox"
REM pytest -s -v -m "sanity" --html=reports/automation_report.html --self-contained-html --browser="firefox"

:: 4. CRITICAL: Keep the command prompt window open after execution finishes or crashes
pause
