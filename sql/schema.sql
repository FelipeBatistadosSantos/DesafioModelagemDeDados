-- Criação da tabela Movies
CREATE TABLE IF NOT EXISTS Movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rank INTEGER,
    title TEXT UNIQUE NOT NULL,
    genre TEXT,
    description TEXT,
    director TEXT,
    year INTEGER,
    runtime INTEGER,
    rating REAL,
    votes INTEGER,
    revenue REAL,
    metascore INTEGER
);

-- Criação da tabela Actors
CREATE TABLE IF NOT EXISTS Actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

-- Criação da tabela MovieActors (associação entre filmes e atores)
CREATE TABLE IF NOT EXISTS MovieActors (
    movie_id INTEGER,
    actor_id INTEGER,
    FOREIGN KEY(movie_id) REFERENCES Movies(id),
    FOREIGN KEY(actor_id) REFERENCES Actors(id),
    PRIMARY KEY (movie_id, actor_id)
);
