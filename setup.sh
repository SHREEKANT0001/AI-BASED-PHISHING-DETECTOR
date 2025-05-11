#!/bin/bash

echo "🔧 Setting up the phishing detector..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run the Flask app
echo "🚀 Running the app on http://localhost:10000"
python app.py