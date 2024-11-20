-- Lists all shows contained in hbtn_0d_tvshows without a genre linked
-- Each record should display: tv_show.title - tv_show_genres.genre-id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- The database name will be passed as argument of the mysql commmand

SELECT ts.title, tsg.genre_id
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
WHERE tsg.show_id IS NULL
ORDER BY ts.title ASC, tsg.genre_id ASC;
