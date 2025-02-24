@echo off
REM Set the PowerShell execution policy for the current user
powershell.exe -Command "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force" > C:\SRSBot\watcher_output.txt 2>&1

REM Run the watcher PowerShell script in hidden mode and log output
powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File "C:\SRSBot\watcher.ps1" >> C:\SRSBot\watcher_output.txt 2>&1

echo. > C:\SRSBot\trigger.txt
timeout /t 7 /nobreak
echo. > C:\SRSBot\trigger.txt