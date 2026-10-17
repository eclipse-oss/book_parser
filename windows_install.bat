@echo off
# Set the console code page to UTF-8 to correctly display special characters
chcp 65001 > nul
echo === Starting project installation ===

# Clone the repository from GitHub
echo Cloning the repository from GitHub...
git clone https://github.com/eclipse-oss/book_parser

# Check if the git clone command failed and handle the error
if %errorlevel% neq 0 (
    echo [Error] Failed to clone the repository. Check your Git installation and the link.
    pause
    exit /b
)

# Navigate into the project folder
cd book_parser

# Create an isolated Python virtual environment named 'venv'
echo Creating a virtual environment (venv)...
python -m venv venv

# Check if the virtual environment creation failed and handle the error
if %errorlevel% neq 0 (
    echo [Error] Failed to create venv. Ensure that Python has been added to the PATH.
    pause
    exit /b
)

echo Updating pip and installing libraries...

# Activate the virtual environment
call venv\Scripts\activate

# Upgrade pip and install base packages inside the virtual environment
python -m pip install --upgrade pip
python -m pip install requests beautifulsoup4 lxml

# Check for a requirements.txt file and install dependencies if it exists
if exist requirements.txt (
    pip install -r requirements.txt
) else (
    echo [Warning] The requirements.txt file was not found.
)

echo === Installation completed successfully! ===
pause