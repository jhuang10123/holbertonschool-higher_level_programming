--  lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each.
SELECT `tv_genres.name`, COUNT(*) as `number of shows`
FROM 
WHERE `tv_genres.show_id` NOT NULL;
ORDER BY tv_genres.name DESC, number of shows DESC;
