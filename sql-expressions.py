from sqlalchemy import(
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# creating an object to execute the queries from the local database chinook

db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# Now we need to create varibles for the tables

artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)

)

album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))

)

track_table = Table (
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)


# this part is to make the connection

with db.connect() as connection:
    #QUery 1 select all the artists from table "Artist"

    #first we create a select_query varible to store all the queries
    # select_query = artist_table.select()
    #---------------------------------------------------------------------------------#

    # Query 2 getting only the "Name" from the artist table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])
    #---------------------------------------------------------------------------------#

    # Query 3 selectiong only "Queen" from the artist table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")
    #---------------------------------------------------------------------------------#


    # Query 4 selecting only by "ArtistId" from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)
    #---------------------------------------------------------------------------------#

    # Query 5 Seletc only the albuns with "ArtistId" on "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)
    #---------------------------------------------------------------------------------#

    #Query 6 select all "tracks" where composer is "queen"
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    # then all the results will be store in the varible results
    results = connection.execute(select_query)

    # so we can iterate on it and print each one 

    for result in results:
        print(result)