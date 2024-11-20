-- Lists all cities contained in the databas hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- The database nae will be passed as an argument of the mysql command

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON states.id = cities.state_id
ORDER BY cities.id ASC;
