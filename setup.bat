@echo off
echo ================================================
echo LeetCode Typer - Setup Installer
echo ================================================
echo.
echo This will install all required dependencies...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

echo Python found:
python --version
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
echo.

REM Install dependencies
echo Installing dependencies from requirements.txt...
python -m pip install -r requirements.txt
echo.

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies!
    echo Please check your internet connection and try again.
    echo.
    pause
    exit /b 1
)

echo.
echo ================================================
echo Setup completed successfully!
echo ================================================
echo.
echo You can now run the app using "run.bat"
echo.
pause

