--  lists all shows contained in hbtn_0d_tvshows with at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows_genres
JOIN tv_shows
ON tv_show_genres.genre_id=tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
