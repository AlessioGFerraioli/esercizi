import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

#print(mydb)

mycursor = mydb.cursor()

#query = "CREATE DATABASE PYTHONMYSQL"

query = "show databases"

mycursor.execute(query)

for x in mycursor:
    print(x)