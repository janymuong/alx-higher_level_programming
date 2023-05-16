-- MSQL: script lists all records of the table second_table; all fileds except name
SELECT score, name FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
