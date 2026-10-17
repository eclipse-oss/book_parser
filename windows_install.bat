@echo off
chcp 65001 > nul
echo === Starting project installation ===

echo Cloning the repository from GitHub...
git clone https://github.com/eclipse-oss/book_parser
if %errorlevel% neq 0 (
    echo [Error] Failed to clone the repository. Check your Git installation and the link.
    pause
    exit /b
)

cd book_parser

echo Creating a virtual environment (venv)...
python -m venv venv
if %errorlevel% neq 0 (
    echo [Error] Failed to create venv. Ensure that Python has been added to the PATH.
    pause
    exit /b
)

echo Updating pip and installing libraries...
call venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install requests beautifulsoup4 lxml

if exist requirements.txt (
    pip install -r requirements.txt
) else (
    echo [Warning] The requirements.txt file was not found.
)

echo === Installation completed successfully! ===
pause