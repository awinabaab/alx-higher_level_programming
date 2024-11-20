-- Lists all genre from hbtn_0d_tvshow and displays the number of shows linked to each
-- Each record should display <TV show genre> - <Number of shows like to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Genres without any linked show won't be displayed
-- Result must be displayed in descending order by the number of shows linked
-- The database name will be passed as an argument of the mysql command

SELECT tg.name AS genre, COUNT(tsg.genre_id) AS number_of_shows
FROM tv_genres tg
JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
WHERE tsg.show_id IS NOT NULL
GROUP BY tg.name
ORDER BY number_of_shows DESC;
