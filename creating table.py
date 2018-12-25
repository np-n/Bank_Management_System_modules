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

# for table creation
# my_cursor.execute("CREATE TABLE users(name  VARCHAR(255), password VARCHAR(255),email VARCHAR(255))")
sqlinput="INSERT INTO users(name,password,email) VALUES(%s,%s,%s)"
records=[
("netra","netra123","nimesh.neupane43@gmail.com"),
("John","john123","john44@gmail.com"),
("mark","mark","mark44@gmail.com"),
("nishan","nishan344","nishan676@gmail.com"),
("kerl","kera879","kera43@gmail.com")

]
my_cursor.executemany(sqlinput,records)
mydb.commit()
