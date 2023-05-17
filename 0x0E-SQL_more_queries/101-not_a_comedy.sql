-- MySQL: a script that lists all shows without the genre Comedy in the database

-- list shows without the genre Comedy
SELECT DISTINCT t.`title`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s ON s.`show_id` = t.`id`
LEFT JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`
WHERE g.`name` != "Comedy" OR g.`name` IS NULL
ORDER BY t.`title`;
