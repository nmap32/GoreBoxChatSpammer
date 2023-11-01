@echo off
:loop
tasklist /fi "imagename eq py.exe" | find /i "py.exe" > nul
if %errorlevel% neq 0 (
    start "" "C:\GoreBoxChatSpammer.py"
)
timeout /t 1 > nul
goto loop