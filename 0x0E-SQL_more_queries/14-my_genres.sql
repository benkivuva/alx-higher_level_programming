-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT genres.name
FROM tv_show_genres AS show_genres
INNER JOIN tv_shows AS shows ON show_genres.show_id = shows.id AND shows.title = 'Dexter'
INNER JOIN tv_genres AS genres ON genres.id = show_genres.genre_id
ORDER BY genres.name;
