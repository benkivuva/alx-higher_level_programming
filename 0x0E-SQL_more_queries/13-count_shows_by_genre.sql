-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT genres.name AS genre, COUNT(show_genres.show_id) AS number_of_shows
FROM tv_show_genres AS show_genres
INNER JOIN tv_genres AS genres
ON show_genres.genre_id = genres.id
GROUP BY genres.name
ORDER BY number_of_shows DESC;
