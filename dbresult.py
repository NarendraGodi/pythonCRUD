import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="godi",
    passwd="godi",
    database="flaskapp"
)

my_cursor = mydb.cursor()

my_cursor.execute("select * from users")

result = my_cursor.fetchall()

print(result[1][1])

