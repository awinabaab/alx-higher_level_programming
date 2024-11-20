-- Lists all shows contained in the dtabas hbtn_0d_tvshows
-- Each record should display tv_show.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Displays NULL if a show doesn't have a genre
-- The database name will be passed as an argument of the mysql command

SELECT ts.title, tsg.genre_id
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
ORDER BY ts.title ASC, tsg.genre_id ASC;
