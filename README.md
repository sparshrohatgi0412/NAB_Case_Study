# NAB_Case_Study

# Project structure

nab_case_study/ <br />
├── netflix_titles.csv             # Original data  <br />
├── config.yaml                    # Configuration file <br />
├── clean_netflix_data.py          # Python cleaning logic <br />
├── requirements.txt               # Python dependencies <br />
├── run_cleaning.sh                # Automation script (optional) <br />
├── netflix_cleaned.csv            # Cleaned output file (Power BI uses this) <br />
├── nab_case_study.pbix            # Power BI presentation file <br />
├── nab_case_study.pdf             # Power BI presentation pdf <br />

# Run manually without shell script

python3 -m venv venv <br />
source venv/bin/activate <br />
pip install -r requirements.txt <br />
python clean_netflix_data.py <br />


#  Run using shell script

./run_cleaning.sh


