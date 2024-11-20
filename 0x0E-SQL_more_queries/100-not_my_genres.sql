-- Uses the hbtn_0d_tvshows database to list all genres not linked to the hsow Dexter
-- Each record should display: tv_genres.name
-- Results should be sorted in ascending order by the genre name
-- The database name will be passed as an argument of the MySQL command

SELECT tg.name
FROM tv_genres tg
WHERE tg.id NOT IN (
	SELECT tv_genres.id
	FROM tv_genres
	JOIN tv_shows ts
	JOIN tv_show_genres tsg
	ON tsg.show_id = ts.id
	ON tsg.genre_id = tg.id
	WHERE ts.title = 'Dexter'
)
ORDER BY tg.name ASC;
