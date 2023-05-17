-- MySQL: Write a script that creates the table, with column w/ UNIQUE column field, a default
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
