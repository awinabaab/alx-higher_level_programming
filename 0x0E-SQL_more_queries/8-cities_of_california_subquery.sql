-- Lists all the cities of California that can be found in the database hbtn_0d_usa
-- The states table contains only one record where name = California
-- Results must be sorted in the ascending order by cities.id
-- The database name will be passed as an argument of the mysql command

SELECT id, name FROM cities WHERE state_id = 1;
