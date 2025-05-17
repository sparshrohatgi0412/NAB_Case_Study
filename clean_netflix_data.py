import pandas as pd
import yaml

def load_config(config_path='config.yaml'):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def clean_netflix_data():
    # Load configuration
    config = load_config()
    input_path = config['input_path']
    output_path = config['output_path']
    valid_ratings = config['valid_ratings']
    columns_to_fill = config['columns_to_fill_na']

    # Load dataset
    dataset = pd.read_csv(input_path)

    # Clean column names
    dataset.columns = dataset.columns.str.strip().str.lower().str.replace(' ', '_')

    # Fix invalid rating values
    invalid_rating_mask = ~dataset['rating'].isin(valid_ratings)
    dataset.loc[invalid_rating_mask & dataset['duration'].isna(), 'duration'] = dataset.loc[invalid_rating_mask, 'rating']
    dataset.loc[invalid_rating_mask, 'rating'] = 'Unknown'

    # Fill missing values
    for col in columns_to_fill:
        dataset[col].fillna('Unknown', inplace=True)

    # Convert and extract date fields
    dataset['date_added'] = pd.to_datetime(dataset['date_added'], errors='coerce')
    dataset['year_added'] = dataset['date_added'].dt.year
    dataset['month_added'] = dataset['date_added'].dt.month_name()

    # Handle genres (one-hot encoding)
    dataset['genres'] = dataset['listed_in'].str.split(', ')
    genres_exploded = dataset[['show_id', 'genres']].explode('genres')
    genre_dummies = pd.get_dummies(genres_exploded['genres'])
    genre_counts = genres_exploded.join(genre_dummies).groupby('show_id').sum()

    # Merge encoded genres back
    dataset = dataset.merge(genre_counts, on='show_id', how='left')

    # Save cleaned dataset
    dataset.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}")

# Run when script is executed directly
if __name__ == '__main__':
    clean_netflix_data()