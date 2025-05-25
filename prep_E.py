import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='Animali'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Mammiferi WHERE Peso > 2")
records = mycursor.fetchall()

for row in records:
    print(row)