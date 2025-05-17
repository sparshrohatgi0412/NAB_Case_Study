# NAB_Case_Study

<!-- Project structure -->

nab_case_study/
├── netflix_titles.csv              # Original data
├── config.yaml                     # Configuration file
├── clean_netflix_data.py          # Python cleaning logic
├── requirements.txt               # Python dependencies
├── run_cleaning.sh                # Automation script (optional)
└── netflix_cleaned.csv            # Cleaned output file (Power BI uses this)

<!-- Run manually without shell script -->

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python clean_netflix_data.py


<!-- Run using shell script -->

./run_cleaning.sh

<!-- End -->
