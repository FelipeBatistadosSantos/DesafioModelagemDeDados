import pandas as pd
from unidecode import unidecode

def preprocess_csv():
    df = pd.read_csv('data/IMDB-Movie-Data.csv')

    df['Actors'] = df['Actors'].apply(lambda x: ', '.join(unidecode(actor.strip()) for actor in x.split(',')))

    df.to_csv('data/IMDB-Movie-Data-Processed.csv', index=False)

if __name__ == "__main__":
    preprocess_csv()
