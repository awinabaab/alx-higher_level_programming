-- Lists the number of recors with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server
-- 
-- The results should display:
	-- the score
	-- the number of records for this score with the label number
-- The list should be sorted by the number of records(descending)
-- The database name will be passed as an argument of the mysql command

SELECT score, COUNT(score) AS 'number'
FROM second_table
GROUP BY score
ORDER BY 'number' DESC;
