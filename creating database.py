import mysql.connector
mydb=mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="2075project"
)
my_cursor= mydb.cursor()

 my_cursor.execute("CREATE DATABASE data1")   # inorder to create database


