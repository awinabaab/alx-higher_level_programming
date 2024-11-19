-- Converts hbtn_0c_0 database to utf-8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server
-- Converts all the following:
	-- Database hbtn_0c_0
	-- Table first_table
	-- Field name in first_table

USE hbtn_0c_0;

ALTER DATABASE hbtn_0c_0
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
MODIFY name VARCHAR(256)
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
