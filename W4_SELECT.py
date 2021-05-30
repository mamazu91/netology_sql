import os
import sqlalchemy
from pprint import pprint

db = os.getenv('DB_CONNECTION_STRING')
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# Titles and release dates of albums released in 2018
pprint(connection.execute("""
SELECT title, release_date
FROM Albums
WHERE release_date = 2018;
""").fetchall())

# # Name and length of the longest track
pprint(connection.execute("""
SELECT title, length
FROM Tracks
ORDER BY length DESC;
""").fetchone())

# # Names of tracks with length > 3.5 minutes
pprint(connection.execute("""
SELECT title
FROM Tracks
WHERE length::INTEGER >= 210;
""").fetchall())

# Names of mixes released between 2018 and 2020
pprint(connection.execute("""
SELECT name
FROM Mixes
WHERE release_date::INTEGER BETWEEN 2018 and 2020;
""").fetchall())

# # Artists names of which consist of just one word
pprint(connection.execute("""
SELECT name
FROM Artists
WHERE name NOT LIKE '%% %%';
""").fetchall())

# # Titles of tracks that contain 'my' in their names
pprint(connection.execute("""
SELECT title
FROM Tracks
WHERE title iLIKE '%%my%%';
""").fetchall())
