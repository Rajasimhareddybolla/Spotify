-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database
UPDATE SPOTIFY_SONGS
SET classification =
    CASE 
        WHEN popularity >= 80 THEN 'Very Popular'
        WHEN popularity >= 60 THEN 'Popular'
        WHEN popularity >= 40 THEN 'Moderately Popular'
        ELSE 'Less Popular'
    END;

INSERT INTO "data" ("song_id", "Enerygy", "KEY", "loudness", "mode", "speechiness", "instrumentalness", "liveness", "valence",  "genere", "classification", "id")
SELECT "id", "Enerygy", "KEY", "loudness", "mode", "speechiness", "instrumentalness", "liveness", "valence",  "genere", "classification", "id"
FROM "SPOTIFY_SONGS";

SELECT COUNT(*) FROM SPOTIFY_SONGS WHERE classification = 'Very Popular';
SELECT count(*) FROM SPOTIFY_SONGS WHERE classification = 'Popular';
SELECT count(*) FROM SPOTIFY_SONGS WHERE classification = 'Moderately Popular';
SELECT count(*) FROM SPOTIFY_SONGS WHERE classification = 'Less Popular'

SELECT count(*),year FROM SPOTIFY_SONGS GROUP BY year ORDER BY year ;

SELECT *
FROM SPOTIFY_SONGS
WHERE speechiness > 0.8 AND instrumentalness < 0.1;

SELECT genere, AVG(Enerygy) AS avg_energy, AVG(loudness) AS avg_loudness
FROM SPOTIFY_SONGS
WHERE explicit = 'False'
GROUP BY genere;

SELECT KEY, COUNT(*) AS key_count
FROM SPOTIFY_SONGS
GROUP BY KEY
ORDER BY key_count DESC;

SELECT classification, SUM(duration_ms) AS total_duration
FROM SPOTIFY_SONGS
GROUP BY classification;

SELECT artist, COUNT(*) AS explicit_count
FROM SPOTIFY_SONGS
WHERE explicit = 'True'
GROUP BY artist
ORDER BY explicit_count DESC
LIMIT 1;