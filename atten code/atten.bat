ECHO ON
REM A batch script to execute a Python script
SET PATH=%PATH%;C:\Python27
START /B python attendance_trial.py
ECHO %time%
timeout 25 > NUL
ECHO %time%
taskkill /IM cmd.exe /FI "WINDOWTITLE eq launcher*"