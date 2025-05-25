import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='Animali'
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
val = [
    ('Fido', 'Labrador', 30, 5),
    ('Kitty', 'Siamese', 4, 2),
    ('Leo', 'Leone', 190, 8),
    ('Dumbo', 'Elefante', 5000, 15),
    ('Speedy', 'Ghepardo', 55, 3)
]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inseriti.")