-- Lists all Comedy show in the database hbtn_0d_tvshows
-- Each record show display tv_shows.title
-- Results must be sorted in ascending order by the show title
-- The database name will be passed as an argument of the mysql command

SELECT ts.title
FROM tv_shows ts
JOIN tv_genres tg
JOIN tv_show_genres tsg
ON tsg.genre_id = tg.id
ON tsg.show_id = ts.id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;
