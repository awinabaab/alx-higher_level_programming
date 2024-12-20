-- Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server
-- unique_id description:
	-- id unique, auto generated, can't be null and is the primary key
	-- name VARCHAR(256) can't be null
-- If the database hbtn_0d_usa already exists, the script should not fail
-- If the table states already exists, the script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
	name VARCHAR(256) NOT NULL
)
