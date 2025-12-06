@echo off
title Fix One-Liner Issue
color 0E

echo.
echo  ====================================================
echo    LeetCode Typer - One-Liner Issue Fix
echo  ====================================================
echo.
echo  This will increase timing delays to fix the
echo  one-liner output problem.
echo.
echo  ====================================================
echo.

REM Create a Python script to modify the configuration
echo import re > temp_fix.py
echo. >> temp_fix.py
echo with open('multilanguage typer.py', 'r', encoding='utf-8') as f: >> temp_fix.py
echo     content = f.read() >> temp_fix.py
echo. >> temp_fix.py
echo # Replace the configuration values >> temp_fix.py
echo content = re.sub(r'LINE_BREAK_DELAY = 0\.\d+', 'LINE_BREAK_DELAY = 0.25', content) >> temp_fix.py
echo content = re.sub(r'AUTO_INDENT_WAIT = 0\.\d+', 'AUTO_INDENT_WAIT = 0.30', content) >> temp_fix.py
echo. >> temp_fix.py
echo with open('multilanguage typer.py', 'w', encoding='utf-8') as f: >> temp_fix.py
echo     f.write(content) >> temp_fix.py
echo. >> temp_fix.py
echo print('Configuration updated successfully!') >> temp_fix.py

REM Run the Python script
python temp_fix.py

if errorlevel 1 (
    echo.
    echo  ERROR: Could not update configuration!
    echo  Please manually edit multilanguage typer.py
    echo.
    del temp_fix.py
    pause
    exit /b 1
)

REM Clean up
del temp_fix.py

echo.
echo  ====================================================
echo   Fix Applied Successfully!
echo  ====================================================
echo.
echo  Changes made:
echo   - LINE_BREAK_DELAY increased to 0.25
echo   - AUTO_INDENT_WAIT increased to 0.30
echo.
echo  Now run the app using run.bat
echo  The one-liner issue should be resolved!
echo.
echo  ====================================================
echo.
pause

