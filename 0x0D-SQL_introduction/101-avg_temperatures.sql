-- MYSQL: a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- dump content in command-line like this: mysql db_name < path/to/dump_file.sql

SELECT city, AVG(`value`) AS avg_temp
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
