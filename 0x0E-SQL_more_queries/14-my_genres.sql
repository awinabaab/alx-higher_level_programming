-- Uses the hbtn_0d_tvshows database to list all genres of the show Dexter
-- Each record show display: tv_geners.name
-- Result mut be sorted in ascending order by the genre name
-- The database name will be passed as an argument of the mysql command

SELECT tg.name
FROM tv_genres tg
JOIN tv_show_genres tsg
JOIN tv_shows ts
ON tsg.show_id = ts.id
ON tsg.genre_id = tg.id
WHERE ts.title = 'Dexter'
ORDER BY tg.name ASC;
