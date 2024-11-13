import mysql.connector

'''
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)



#print(mydb)

#mycursor = mydb.cursor()
# crea database
#query = "CREATE DATABASE PYTHONMYSQL"
# mycursor.execute(query)

# show databases
query = "show databases"
mycursor.execute(query)
for x in mycursor:
    print(x)

'''

# fare il connector con un solo database (invece che tutti quello sull'host)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "pythonmysql"
)
# creo un cursore per questo connector "mydb" che contiene solo il database "pythonmysql"
mycursor = mydb.cursor()

#creo una query per creare tabella
query = "CREATE TABLE utenti (ID int auto_increment primary key, nome VARCHAR(50), indirizzo VARCHAR(50))"
mycursor.execute(query)

# mostrare le tables
query = "SHOW TABLES"
mycursor.execute(query)
for x in mycursor:
    print(x)