@echo off
:: 1. Force Jenkins to append your system Python installation to its PATH
SET PATH=C:\Users\seetharamaraju\AppData\Local\Programs\Python\Python314;C:\Users\seetharamaraju\AppData\Local\Programs\Python\Python314\Scripts;%PATH%

:: 2. Check if a virtual environment exists in the Jenkins workspace; if not, create it
if not exist .venv (
    echo ⚙️ Creating a fresh virtual environment in Jenkins workspace...
    python -m venv .venv
)

:: 3. Activate the workspace virtual environment
call .venv\Scripts\activate

:: 4. Upgrade pip and install all project dependencies from your requirements.txt file
echo 📦 Installing framework dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

:: 5. Finally, execute your tests safely
echo 🚀 Launching Pytest execution...
pytest -s -v -m "regression" --html=reports/automation_report.html --self-contained-html --browser="chrome"

rem pytest -s -v -m "sanity" --html=reports/automation_report.html --self-contained-html --browser="chrome"
rem pytest -s -v -m "regression" --html=reports/automation_report.html --self-contained-html --browser="edge"
rem pytest -s -v -m "sanity" --html=reports/automation_report.html --self-contained-html --browser="edge"
rem pytest -s -v -m "regression" --html=reports/automation_report.html --self-contained-html --browser="firefox"
rem pytest -s -v -m "sanity" --html=reports/automation_report.html --self-contained-html --browser="firefox"

:: 6. CRITICAL: Keep the command prompt window open after execution finishes or crashes
pause