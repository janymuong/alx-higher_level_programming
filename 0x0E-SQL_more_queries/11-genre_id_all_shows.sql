-- MySQL: ist all shows with their genre IDs or NULL if no genre exists

SELECT tv_shows.title, tv_show_genres.genre_id
FROM `tv_shows`
LEFT JOIN `tv_show_genres` ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
