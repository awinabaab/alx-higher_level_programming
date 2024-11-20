-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- The database name will be paassed as an argument of the mysql command

SELECT tg.name, SUM(tsr.rate) AS rating
FROM tv_genres tg
JOIN tv_show_ratings tsr
JOIN tv_show_genres tsg
ON tsg.show_id = tsr.show_id
ON tsg.genre_id = tg.id
GROUP BY tg.name
ORDER BY rating DESC;
