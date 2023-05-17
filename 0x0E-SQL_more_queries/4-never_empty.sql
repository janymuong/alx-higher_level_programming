-- MySQL: Write a script that creates the table, with column w/ a default_val
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
