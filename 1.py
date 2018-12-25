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
# Insert in to database
# sqlinput="INSERT INTO users(name,password,email) VALUES(%s,%s,%s)"
# records=[
# ("netra","netra123","nimesh.neupane43@gmail.com"),
# ("John","john123","john44@gmail.com"),
# ("mark","mark","mark44@gmail.com"),
# ("nishan","nishan344","nishan676@gmail.com"),
# ("kerl","kera879","kera43@gmail.com")

# ]
# my_cursor.executemany(sqlinput,records)
# mydb.commit()
# inorder to select and fetch all
# my_cursor.execute(" SELECT *  FROM  users ")
# result=my_cursor.fetchall()
# for row in result :
#    print(row)
'''
# inorder to select one items-email from database
my_cursor.execute(" SELECT *  FROM  users ")
result = my_cursor.fetchall()
print("name \t password \t\temail")
print("-----\t---------\t\t-------")
for row in result:
    print(" %s " %row[0] + " \t%s "%row[1]+"\t\t%s "%row[2])
'''
 # where clause inorder to check and search database content
 # my_cursor.execute("SELECT * FROM users WHERE name='netra'")
# my_cursor.execute("SELECT * FROM users WHERE name LIKE 'netra'") # only search for netra


# my_cursor.execute("SELECT * FROM users WHERE name LIKE 'ne%'AND password=0")
# result=my_cursor.fetchall()
# for db in result:
#  print(db)

'''
my_cursor.execute("SELECT * FROM users WHERE name LIKE 'ne%' AND  password=0") # Search only database starting with ne and password 0
# you can do OR  also in the place of AND
result = my_cursor.fetchall()
for db in result:
    print(db)
'''
'''# updating in to database
update="UPDATE users SET name='Bikash' WHERE email='kera43@gmail.com'"
my_cursor.execute(update)
mydb.commit()
'''
# appending into table
#  datainput="INSERT INTO users(name,password,email) VALUES(%s,%s,%s)"
# append_record=('Hkjdfkd',3287489,'hk88@gmil.com')
# my_cursor.execute(datainput,append_record)
# mydb.commit()
'''
my_cursor.execute("SELECT * FROM users LIMIT 5 ") # selecting 3 row from table
# you can do OR  also in the place of AND
result = my_cursor.fetchall()
for db in result:
    print(db)
'''
'''
my_cursor.execute("SELECT * FROM users LIMIT 5 OFFSET 1") # selecting 3 row from table
# you can do OR  also in the place of AND
result = my_cursor.fetchall()
for db in result:
    print(db)
'''
'''
# sorting in ascending order
my_cursor.execute("SELECT * FROM users  ORDER BY name ASC") # ASC for ascending sorting
# you can do OR  also in the place of AND
result = my_cursor.fetchall()
for db in result:
    print(db)
'''
# sorting in descending order order
my_cursor.execute("SELECT * FROM users  ORDER BY name DESC") # ASC for ascending sorting
# you can do OR  also in the place of AND
result = my_cursor.fetchall()
for db in result:
    print(db)

# delete column
delete_user=" DELETE FROM users WHERE name='nishan'"
my_cursor.execute(delete_user)
mydb.commit()
