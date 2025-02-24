@echo off
timeout /t 5 /nobreak

:loop
if exist C:\SRSBot\trigger.txt (
    start C:\SRSBot\start_bot.bat
    del C:\SRSBot\trigger.txt
    goto loop
) else (
    cls
    timeout /t 5 /nobreak
    goto loop
)
