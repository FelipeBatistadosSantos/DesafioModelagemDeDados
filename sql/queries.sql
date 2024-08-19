SELECT a.name, COUNT(ma.movie_id) AS num_movies
FROM Actors a
JOIN MovieActors ma ON a.id = ma.actor_id
GROUP BY a.id
ORDER BY num_movies DESC, a.name;

SELECT a.name, AVG(m.rating) AS avg_rating
FROM Actors a
JOIN MovieActors ma ON a.id = ma.actor_id
JOIN Movies m ON ma.movie_id = m.id
GROUP BY a.id;

SELECT title, rating
FROM Movies
WHERE rating > (SELECT AVG(rating) FROM Movies);

SELECT title, votes
FROM Movies
WHERE votes > 10000;
