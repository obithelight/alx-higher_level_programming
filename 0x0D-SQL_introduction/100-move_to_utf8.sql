-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server

-- Use the hbtn_0c_0 database
USE hbtn_0c_0;

-- Convert all tables in the database to utf8mb4 character set and utf8mb4_unicode_ci collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert all existing tables and their columns to utf8mb4 character set and utf8mb4_unicode_ci collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- If you have multiple tables, repeat the ALTER TABLE command for each table
-- ALTER TABLE another_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
