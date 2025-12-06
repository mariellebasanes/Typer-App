@echo off
title LeetCode Typer - Multi-Language

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please run setup.bat first to install dependencies.
    echo.
    pause
    exit /b 1
)

REM Run the Python script
python "multilanguage typer.py"

REM Keep window open if there was an error
if errorlevel 1 (
    echo.
    echo An error occurred!
    pause
)

