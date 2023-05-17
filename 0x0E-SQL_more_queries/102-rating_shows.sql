-- MySQL: lists all shows from hbtn_0d_tvshows_rate by their rating; sort in desc order by title

-- use the not hbtn_0d_tvshows_rate database
USE `hbtn_0d_tvshows`;

SELECT t.title, SUM(r.rating) AS rating
FROM tv_shows AS t
JOIN rating AS r ON r.show_id = t.id
GROUP BY t.title
ORDER BY rating DESC;
