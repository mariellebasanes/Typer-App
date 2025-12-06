@echo off
title LeetCode Typer - Quick Installer
color 0A

echo.
echo  ====================================================
echo    LeetCode Typer - Multi-Language Code Typer
echo  ====================================================
echo.
echo  This installer will:
echo   1. Check if Python is installed
echo   2. Install required dependencies
echo   3. Launch the application
echo.
echo  ====================================================
echo.

REM Check if Python is installed
echo [1/3] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo  ERROR: Python is NOT installed!
    echo.
    echo  Please install Python 3.7 or higher from:
    echo  https://www.python.org/downloads/
    echo.
    echo  IMPORTANT: During installation, check the box:
    echo  "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo  Python found: 
python --version
echo.

REM Check if dependencies are already installed
echo [2/3] Checking dependencies...
python -c "import pyperclip, pyautogui" >nul 2>&1
if errorlevel 1 (
    echo  Installing dependencies...
    echo.
    
    REM Upgrade pip first
    python -m pip install --upgrade pip --quiet
    
    REM Install dependencies
    python -m pip install -r requirements.txt --quiet
    
    if errorlevel 1 (
        echo.
        echo  ERROR: Failed to install dependencies!
        echo  Please check your internet connection.
        echo.
        pause
        exit /b 1
    )
    
    echo  Dependencies installed successfully!
) else (
    echo  Dependencies already installed!
)
echo.

echo [3/3] Launching LeetCode Typer...
echo.
echo  ====================================================
echo.

REM Run the application
python "multilanguage typer.py"

REM Pause if there was an error
if errorlevel 1 (
    echo.
    echo  An error occurred while running the application.
    pause
)

