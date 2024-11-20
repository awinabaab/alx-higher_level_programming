-- Lists all show,a nd all genres linked to that show, from the database hbtn_0d_tvshows
-- If a show doesnt have a genre, display NULL in the genre column
-- Each recored should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- The database name will be passed as an argument of the mysql command

SELECT ts.title, tg.name
FROM tv_shows ts
LEFT JOIN tv_genres tg
JOIN tv_show_genres tsg
ON tsg.genre_id = tg.id
ON tsg.show_id = ts.id
ORDER BY ts.title ASC, tg.name ASC;
