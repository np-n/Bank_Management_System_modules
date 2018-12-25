import mysql.connector
mydb=mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="2075project",
    database="data1"
)
# create cursor instance
my_cursor= mydb.cursor()

# create database
# my_cursor.execute("CREATE DATABASE data1")   inorder to create database
# show database
# my_cursor.execute("SHOW DATABASES")
#for db in my_cursor :
#    print(db[0])   # produce output without any parenthesis rather than print(db)

my_cursor.execute("CREATE TABLE users(name  VARCHAR(255), password INTEGER(255),email VARCHAR(255))")
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table)