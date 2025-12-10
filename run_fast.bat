@echo off
REM Simple runner for Multi-Language Code Typer (fast settings)
REM Requires Python 3.7+ on PATH

set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

REM Install dependencies (no-ops if already installed)
py -3 -m pip install -r requirements.txt >nul

REM Launch the typer
py -3 "multilanguage typer.py"

