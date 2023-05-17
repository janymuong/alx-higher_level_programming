-- MySQL: a script that lists all shows contained in db w/ at least one genre linked

-- the hbtn_0d_tvshows database will be passed in as command-line arg
SELECT tv_shows.title, tv_show_genres.genre_id
FROM `tv_shows`
JOIN `tv_show_genres` ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
