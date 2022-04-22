import psycopg2


# connect to chinnok database
connection = psycopg2.connect(database="chinnok")


# build a curser object of the database
cursor = connection.cursor()


# query 1 select all records from the Artist table
cursor.execute('SELECT * FROM "Artist"')


# to fetch multiple results
results = cursor.fetchall()

# close the connection
connection.close()

# to print results
for result in results:
    print(result)