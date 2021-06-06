import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "INSERT INTO aku (id,name) VALUES (%s,%s)"
val = (20,"ERIK")
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

print(mydb)