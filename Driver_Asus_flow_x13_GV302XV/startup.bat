@echo off

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python n'est pas installe. Telechargement de l'installateur...

    set "PYTHON_INSTALLER=https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe"

    powershell -Command "Invoke-WebRequest -Uri %PYTHON_INSTALLER% -OutFile python_installer.exe"

    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    del python_installer.exe

    echo Python a ete installe avec succes.
) ELSE (
    echo Python est deja installe. 
)
timeout /t 3 /nobreak >nul
python main.py
