
import mysql.connector
import base64
import io

import PIL.Image
with open('sarangkot.jpg', 'rb') as f:
    photo = f.read()
encodestring = base64.b64encode(photo)
db= mysql.connector.connect(
    user="root",
    password="2075project",
    host="localhost",
    database="image_insertion")

mycursor=db.cursor()
sql = "insert user_image values(%s)"
mycursor.execute(sql,(encodestring,))
db.commit()
'''
sql1="select * from sample"
mycursor.execute(sql1)
data = mycursor.fetchall()
data1=base64.b64decode(data[0][0])
file_like=io.BytesIO(data1)
img=PIL.Image.open(file_like)
img.show()
db.close()
'''