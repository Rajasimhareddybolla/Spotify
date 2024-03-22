-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it

 .import songs_normalize.csv --csv songs
CREATE TABLE IF NOT EXISTS "SPOTIFY_SONGS"(
"artist" TEXT,
"Song" TEXT,
"duration_ms" INT,
"explicit" blob,
"year" INT,
"popularity" INT,
"danceability" BLOB,
"Enerygy" INT,
"KEY" INT,
"loudness" INT,
"mode" INT,
"speechiness" INT,
"instrumentalness" NUMERIC,
"liveness" INT,
"valence" INT,
"genere" TEXT,
"id" INT,
PRIMARY KEY ("id"));

CREATE TABLE IF NOT EXISTS "songs"(
"artist" TEXT, "song" TEXT, "duration_ms" TEXT, "explicit" TEXT,
 "year" TEXT, "popularity" TEXT, "danceability" TEXT, "energy" TEXT,
 "key" TEXT, "loudness" TEXT, "mode" TEXT, "speechiness" TEXT,
 "acousticness" TEXT, "instrumentalness" TEXT, "liveness" TEXT, "valence" TEXT,
 "tempo" TEXT, "genre" TEXT);

 
create table "data"(
"song_id" INT ,
"Enerygy" INT,
"KEY" INT,
"loudness" INT,
"mode" INT,
"speechiness" INT,
"instrumentalness" NUMERIC,
"liveness" INT,
"valence" INT,
"genere" TEXT,
"classification" TEXT,
"id" INT,
FORIGEN KEY "song_id" REFERENCES "SPOTIFY_SONGS"("id"),
PRIMARY KEY ("id"));


CREATE INDEX "spotify_songs_on_index" on SPOTIFY_SONGS("id","Song","artist","genre","classification");
CREATE INDEX "on_data_index" on data("id","song_id","genere","classification");


CREATE VIEW "User_specific_view" AS
SELECT "Song","classification","genere","popularity","artist","duration_ms" from SPOTIFY_SONGS
;

drop table songs;
