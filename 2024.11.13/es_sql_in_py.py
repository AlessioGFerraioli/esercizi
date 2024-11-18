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

____________________________________________________

#esempio di insert value nella tabella

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "pythonmysql"
)
query = "INSERT INTO utenti (nome,indirizzo) values(%s,%s)"
# valori che vanno passati insieme alla query
valori = ("tommaso", "via roma")
mycursor = mydb.cursor()

mycursor.execute(query, valori)

mydb.commit()

print(mycursor.rowcount, "Record inseriti")


__________________________________________________________


# esempio di select e fetching del risultato della query
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "pythonmysql"
)
mycursor = mydb.cursor()


query = "select * from utenti where nome = %s"

valore = ("tommaso",)

mycursor.execute(query, valore)
risultati = mycursor.fetchall()

print(risultati)


'''


# esempio di select e fetching del risultato della query
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "pythonmysql"
)
mycursor = mydb.cursor()


query = "select * from utenti where nome = %s"

valore = ("tommaso",)

mycursor.execute(query, valore)
risultati = mycursor.fetchall()

print(risultati)