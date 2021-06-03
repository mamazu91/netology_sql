import os
import sqlalchemy

db = os.getenv('DB_CONNECTION_STRING')
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

connection.execute('''
INSERT INTO Artists (Name)
VALUES
('Radiohead'),
('Massive Attack'),
('Nine Inch Nails'),
('Porcupine Tree'),
('Death Grips'),
('AIGEL'),
('TR/ST'),
('Burial');
''')

connection.execute('''
INSERT INTO Genres (Name)
VALUES
('Rock'),
('Triphop'),
('Rap rock'),
('Hip-Hop'),
('Alternative'),
('Electronic');
''')

connection.execute('''
INSERT INTO ArtistsGenres
VALUES
(1, 1),
(1, 2),
(2, 2),
(3, 1),
(3, 5),
(4, 1),
(5, 3),
(6, 4),
(7, 5),
(8, 6);
''')

connection.execute('''
INSERT INTO Albums (title, release_date)
VALUES
('Kid A', '2019'),
('Mezzanine', '2020'),
('Hesitation Marks', '2013'),
('In Absentia', '2002'),
('Money Store', '2018'),
('1190', '2018'),
('TRST', '2012'),
('Burial', '2006');
''')

connection.execute('''
INSERT INTO ArtistsAlbums
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8);
''')

connection.execute('''
INSERT INTO Tracks (album_id, title, length)
VALUES
(1, 'Everything In Its Right Place', '251'),
(1, 'In Limbo', '211'),
(2, 'Angel', '379'),
(2, 'Risinson', '298'),
(3, 'Copy Of A', '322'),
(3, 'Satellite', '302'),
(4, 'Blackest Eyes', '263'),
(4, 'Trains', '358'),
(5, 'Get Got', '171'),
(5, 'Hustle Bones', '192'),
(6, '1190', '312'),
(7, 'Shoom', '326'),
(7, 'Chrissy E', '254'),
(8, 'Distant Lights', '326'),
(8, 'Night Bus', '133');
''')

connection.execute('''
INSERT INTO Mixes (name, release_date)
VALUES
('Top Rock Songs of All Time', '2021'),
('Top Rock Songs of 2000s', '2010'),
('Top Rock Songs of 2010s', '2019'),
('Top Triphop Songs', '2015'),
('Top Rap Rock Songs', '2016'),
('Top Hip-Hop Songs', '2017'),
('Top Alternative Songs', '2018'),
('My Favorite Songs', '2020');
''')

connection.execute('''
INSERT INTO TracksMixes (track_id, mix_id)
VALUES
(1, 1),
(4, 1),
(1, 2),
(2, 2),
(5, 3),
(6, 3),
(3, 4),
(4, 4),
(9, 5),
(10, 5),
(11, 6),
(13, 7),
(14, 7),
(1, 8),
(4, 8),
(15, 8);
''')
