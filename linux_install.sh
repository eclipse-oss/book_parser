#!/bin/bash

# Exit immediately if any command exits with a non-zero status
set -e
echo "=== Starting project installation ==="

# Clone the repository from GitHub and navigate into the project directory
echo "Cloning the repository from GitHub..."
git clone https://github.com/eclipse-oss/book_parser

cd book_parser

# Create an isolated Python virtual environment named 'venv'
echo "Creating a virtual environment (venv)..."
python3 -m venv venv

# Activate the virtual environment, upgrade pip, and install base packages
echo "Updating pip and installing libraries..."
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install requests beautifulsoup4 lxml

# Check for a requirements.txt file and install dependencies if it exists
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo "[Warning] The requirements.txt file was not found."
fi

echo "=== Installation completed successfully! ==="