import mysql.connector
mydb=mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="2075project"
)
my_cursor= mydb.cursor()

# my_cursor.execute("CREATE DATABASE data1")   inorder to create database
my_cursor.execute("SHOW DATABASES")
for db in my_cursor :
    print(db[0])   # produce output without any parenthesis rather than print(db)

