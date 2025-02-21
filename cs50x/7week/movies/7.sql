SELECT movies.title,ratings.rating from ratings
INNER JOIN movies ON movies.id = ratings.movie_id
WHERE movies.year = "2010" ORDER BY ratings.rating DESC,movies.title;