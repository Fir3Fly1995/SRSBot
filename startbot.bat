@echo off
REM Change to the bot files directory
cd %LOCALAPPDATA%\SRSBot\bot_files

REM Activate the virtual environment
call srsenv\Scripts\activate.bat

REM Run the Verifier.py script using the portable Python installation
..\python\python.exe Verifier.py