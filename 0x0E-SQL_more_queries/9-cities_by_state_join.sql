-- MySQL: a script that lists all cities contained in database

-- list all cities with corresponding state names
SELECT cities.id, cities.name, states.name
FROM `cities`
JOIN `states` ON cities.state_id = states.id
ORDER BY cities.id;
