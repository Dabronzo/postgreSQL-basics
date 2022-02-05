import psycopg2

# connect with chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# QUery 1 select all the artists

# cursor.execute('SELECT * FROM "Artist"')
#--------------------------#

# Query 2 getting the name from the artist table

# cursor.execute('SELECT "Name" FROM "Artist"')
#--------------------------#

# Query 3 selectiong only "Queen" from the artist table
#in this case we need to use a python string placeholder %s

# cursor.execute('SELECT * FROM "Artist" WHERE "Name"=%s', ["Queen"])
#--------------------------#

# Query 4 selecting only by "ArtistId" from the "Artist" table

# cursor.execute('SELECT "ArtistId" FROM "Artist"')

# Now selecting by the value 51 "ArtistId" from the "Artist"

# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId"=%s',[51])
#--------------------------#

# Query 5 Seletc only the albuns with "ArtistId" on "Album" table

# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId"=%s', [51])

# Query 6 select all "tracks" where composer is "queen"

cursor.execute('SELECT * FROM "Track" WHERE "Composer"=%s', ["Queen"])


# fetch the results - more than one retrieved in a list
results = cursor.fetchall()

# fetch method to catch only one
# results = cursor.fetchone()

# close the connection
connection.close()

# printing the results
for result in results:
    print(result)