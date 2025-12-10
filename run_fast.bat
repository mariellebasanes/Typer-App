@echo off
REM Multi-Language Code Typer - Fast Launcher
REM Checks for Python and dependencies before running

echo Initializing Multi-Language Code Typer...
echo.

REM 1. Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in your PATH.
    echo Please install Python 3.7+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

REM 2. Install/Update dependencies
echo Checking dependencies...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies.
    echo Please check your internet connection.
    pause
    exit /b 1
)
echo Dependencies are ready.
echo.

REM 3. Run the application
echo Starting the Typer...
python "multilanguage typer.py"

if %errorlevel% neq 0 (
    echo.
    echo [Execution Finished]
    pause
)


