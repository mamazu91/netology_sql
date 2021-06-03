import os
import sqlalchemy
from pprint import pprint

db = os.getenv('DB_CONNECTION_STRING')
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# 1. Number of artists in every genre
pprint(connection.execute("""
SELECT G.name, COUNT(G.name)
FROM Genres G
JOIN ArtistsGenres AG ON G.id = AG.genre_id
JOIN Artists A ON A.id = AG.artist_id
GROUP BY G.name
""").fetchall())

# 2. Number of tracks in albums released between 2019 and 2020
pprint(connection.execute("""
SELECT COUNT(T.title)
FROM Tracks T
JOIN Albums A ON T.album_id = A.id
WHERE A.release_date BETWEEN 2019 AND 2020;
""").fetchall())

# 3. Average length of all tracks for each album
pprint(connection.execute("""
SELECT A.title, ROUND(AVG(T.length::INTEGER))
FROM Tracks T
JOIN Albums A ON T.album_id = A.id
GROUP BY A.title;
""").fetchall())

# 4. Artists that did not release an album in 2020
pprint(connection.execute("""
SELECT AR.name
FROM Artists AR
JOIN ArtistsAlbums ARAL ON AR.id = ARAL.artist_id
JOIN Albums AL ON ARAL.album_id = AL.id
WHERE AL.release_date < 2020
""").fetchall())

# 5. Mixes that contain Radiohead songs
pprint(connection.execute("""
SELECT M.name
FROM Mixes M
JOIN TracksMixes TM ON M.id = TM.mix_id
JOIN Tracks T ON TM.track_id = T.id
JOIN Albums AL ON T.album_id = AL.id
JOIN ArtistsAlbums ARAL ON AL.id = ARAL.album_id
JOIN Artists AR ON ARAL.artist_id = AR.id
WHERE AR.name = 'Radiohead'
""").fetchall())

# 6. Albums written by artists that play in more than 1 genre
pprint(connection.execute("""
SELECT AL.title
FROM Albums AL
JOIN ArtistsAlbums ARAL ON AL.id = ARAL.album_id
JOIN Artists AR ON ARAL.artist_id = AR.id
JOIN ArtistsGenres AG ON AR.id = AG.artist_id
JOIN Genres G ON AG.genre_id = G.id
GROUP BY AL.title
HAVING COUNT(AL.title) > 1;
""").fetchall())

# 7. Tracks not included in any mix
pprint(connection.execute("""
SELECT T.title
FROM Tracks T
LEFT JOIN TracksMixes TM ON T.id = TM.track_id
LEFT JOIN Mixes M ON TM.mix_id = M.id
where M.id is NULL;
""").fetchall())

# 8. Artist(s) with the shortest tracks
pprint(connection.execute("""
SELECT AR.name
FROM Artists AR
JOIN ArtistsAlbums ARAL ON AR.id = ARAL.artist_id
JOIN Albums AL ON ARAL.album_id = AL.id
JOIN Tracks T ON AL.id = T.album_id
WHERE T.length = (SELECT MIN(Tracks.length) FROM Tracks);
""").fetchall())

# 9. Names of albums with the smallest number of tracks
pprint(connection.execute("""
SELECT A.title
FROM Albums A
JOIN Tracks T on A.id = T.album_id
GROUP BY A.title
HAVING COUNT(T.album_id) = (SELECT MIN(C)
FROM (SELECT COUNT(T.album_id) C
FROM Tracks T
GROUP BY T.album_id) tracks_count);
""").fetchall())
