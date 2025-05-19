## This file contains the main function to clean the Netflix dataset.
## It handles loading the configuration, cleaning the data, and saving the cleaned dataset.

import pandas as pd
import yaml

def load_config(config_path='config.yaml'):
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Configuration file {config_path} not found.")
        return {}
    except yaml.YAMLError as e:
        print(f"Error parsing configuration file: {e}")
        return {}

def clean_netflix_data():
    # Load configuration
    try:
        config = load_config()
        input_path = config['input_path']
        output_path = config['output_path']
        valid_ratings = config['valid_ratings']
        columns_to_fill = config['columns_to_fill_na']
    except KeyError as e:
        print(f"Missing configuration key: {e}")
        return

    # Load dataset
    try:
        dataset = pd.read_csv(input_path)
    except FileNotFoundError:
        print(f"Input file {input_path} not found.")
        return
    except pd.errors.EmptyDataError:
        print(f"Input file {input_path} is empty.")
        return

    # Clean column names
    dataset.columns = dataset.columns.str.strip().str.lower().str.replace(' ', '_')

    # Clean all columns: remove newlines and extra spaces
    for col in dataset.columns:
        if dataset[col].dtype == 'object':
            dataset[col] = dataset[col].str.replace('\n', ' ').str.strip().str.replace(' +', ' ')

    # Fix invalid rating values
    invalid_rating_mask = ~dataset['rating'].isin(valid_ratings)
    dataset.loc[invalid_rating_mask & dataset['duration'].isna(), 'duration'] = dataset.loc[invalid_rating_mask, 'rating']
    dataset.loc[invalid_rating_mask, 'rating'] = 'Unknown'

    # Fill missing values
    for col in columns_to_fill:
        dataset[col].fillna('Unknown', inplace=True)

    # Convert and extract date fields
    dataset['date_added'] = dataset['date_added'].astype(str).str.strip()
    dataset['date_added'] = pd.to_datetime(dataset['date_added'], errors='coerce')
    dataset['year_added'] = dataset['date_added'].dt.year
    dataset['month_added'] = dataset['date_added'].dt.month_name()

    # Handle genres (explode)
    dataset['genres'] = dataset['listed_in'].str.split(', ')
    dataset = dataset.explode('genres')
    dataset['genres'] = dataset[ 'genres'].str.strip()

    # Handle country (explode)

    dataset['countries'] = dataset['country'].str.split(', ')
    dataset = dataset.explode('countries')
    dataset['countries'] = dataset['countries'].str.strip()

    # Save cleaned dataset
    dataset.to_csv(output_path, index=False)
    print(f" Cleaned data saved to {output_path}")

# Run when script is executed directly
if __name__ == '__main__':
    clean_netflix_data()