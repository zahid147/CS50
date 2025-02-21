SELECT AVG(ratings.rating) AS Average from ratings
INNER JOIN movies ON movies.id = ratings.movie_id
WHERE movies.year = "2012";