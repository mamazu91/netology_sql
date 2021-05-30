create table if not exists Artists (
id serial primary key,
name varchar not null unique
);

create table if not exists Genres (
id serial primary key,
name varchar not null unique
);

create table if not exists ArtistsGenres (
artist_id integer not null references Artists(id),
genre_id integer not null references Genres(id),
constraint ArtistsGenresPK primary key (artist_id, genre_id)
);

create table if not exists Albums (
id serial primary key,
title varchar not null,
release_date date not null
);

create table if not exists ArtistsAlbums (
artist_id integer not null references Artists(id),
album_id integer not null references Albums(id),
constraint ArtistsAlbumsPK primary key (artist_id, album_id)
);

create table if not exists Tracks (
id serial primary key,
album_id integer not null references Albums(id),
title varchar not null,
length varchar not null
);

create table if not exists Mixes (
id serial primary key,
name varchar not null unique,
release_date date not null
);

create table if not exists TracksMixes (
track_id integer not null references Tracks(id),
mix_id integer not null references Mixes(id),
constraint TracksMixesPK primary key (track_id, mix_id)
);