@echo off
TITLE Multi-Language Typer Setup

echo ========================================================
echo       Multi-Language Code Typer - Setup Wizard
echo ========================================================
echo.

REM 1. Check Python installation
echo [1/2] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is NOT found!
    echo.
    echo Please install Python 3.7 or newer from:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANT: Check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)
python --version
echo Python is installed.
echo.

REM 2. Install Requirements
echo [2/2] Installing required packages...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to install packages.
    echo Please check your internet connection.
    pause
    exit /b 1
)

echo.
echo ========================================================
echo               Setup Completed Successfully!
echo ========================================================
echo.
echo You can now run the application using 'run_fast.bat'
echo.
pause

