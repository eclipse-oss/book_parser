#!/bin/bash
set -e
echo "=== Starting project installation ==="

echo "Cloning the repository from GitHub..."
git clone https://github.com/eclipse-oss/book_parser

cd book_parser

echo "Creating a virtual environment (venv)..."
python3 -m venv venv

echo "Updating pip and installing libraries..."
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install requests beautifulsoup4 lxml

if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo "[Warning] The requirements.txt file was not found."
fi

echo "=== Installation completed successfully! ==="