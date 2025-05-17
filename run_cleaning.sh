#!/bin/bash

echo "🚀 Starting Netflix Data Cleaning Pipeline..."

# Step 1: Set up virtual environment (optional but recommended)
if [ ! -d "venv" ]; then
  echo "📦 Creating virtual environment..."
  python3 -m venv venv
fi

echo "✅ Activating virtual environment..."
source venv/bin/activate

# Step 2: Install required Python packages
echo "📥 Installing required packages from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 3: Run the data cleaning script
echo "🧹 Running data cleaning script..."
python clean_netflix_data.py

# Step 4: Done
echo "🎉 Cleaning complete. Output saved to: $(grep output_path config.yaml | cut -d':' -f2 | xargs)"

# Optional: Deactivate virtual environment
deactivate