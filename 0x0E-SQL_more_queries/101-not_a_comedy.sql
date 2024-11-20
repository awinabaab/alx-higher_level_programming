-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- The database name will be passed as an argument of the mysql command

SELECT ts.title
FROM tv_shows ts
WHERE ts.id NOT IN (
	SELECT tsg.show_id
	FROM tv_show_genres tsg
	JOIN tv_genres tg
	ON tsg.genre_id = tg.id
	WHERE tg.name = 'Comedy'
)
ORDER BY ts.title ASC;
