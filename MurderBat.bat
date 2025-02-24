@echo off
REM Terminate all python.exe processes
taskkill /F /IM python.exe >> C:\SRSBot\murder_log.txt 2>&1

REM Wait for a few seconds
timeout /t 5 /nobreak

REM Start the listener.bat script
start "" cmd.exe /c "C:\SRSBot\listener.bat" >> C:\SRSBot\murder_log.txt 2>&1

REM Optional: Wait a few seconds before completing the script
timeout /t 10 /nobreak
