-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT genres.name, SUM(ratings.rate) AS rating
FROM tv_show_genres AS show_genres
INNER JOIN tv_shows AS shows ON shows.id = show_genres.show_id
INNER JOIN tv_show_ratings AS ratings ON ratings.show_id = shows.id
INNER JOIN tv_genres AS genres ON show_genres.genre_id = genres.id
GROUP BY genres.name
ORDER BY rating DESC;
