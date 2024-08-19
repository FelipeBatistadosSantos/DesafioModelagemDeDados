import pandas as pd
import sqlite3

def insert_data():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    movies_df = pd.read_csv('data/IMDB-Movie-Data-Processed.csv')

    for _, row in movies_df.iterrows():
        movie_id = c.execute("SELECT id FROM Movies WHERE title = ?", (row['Title'],)).fetchone()
        if not movie_id:
            c.execute('INSERT INTO Movies (rank, title, genre, description, director, year, runtime, rating, votes, revenue, metascore) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                      (row['Rank'], row['Title'], row['Genre'], row['Description'], row['Director'], row['Year'], row['Runtime (Minutes)'], row['Rating'], row['Votes'], row['Revenue (Millions)'], row['Metascore']))
            movie_id = c.lastrowid
        else:
            movie_id = movie_id[0]

        actors = [actor.strip() for actor in row['Actors'].split(',')]
        for actor in actors:
            c.execute("INSERT OR IGNORE INTO Actors (name) VALUES (?)", (actor,))
            actor_id = c.execute("SELECT id FROM Actors WHERE name = ?", (actor,)).fetchone()
            
            if actor_id:
                actor_id = actor_id[0]
                c.execute("INSERT OR IGNORE INTO MovieActors (movie_id, actor_id) VALUES (?, ?)", (movie_id, actor_id))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()
