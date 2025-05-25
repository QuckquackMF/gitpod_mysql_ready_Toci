import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='Animali'
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"

try:
    num_animals = int(input("Quanti animali vuoi inserire? "))
    for i in range(num_animals):
        print(f"\nInserisci i dati {i+1}:")
        nome = input("Nome: ")
        razza = input("Razza: ")
        peso = int(input("Peso: "))
        eta = int(input("Eta: "))
        val = (nome, razza, peso, eta)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Animale inserito")
except ValueError:
    print("Stupid: Inserisci un numero intero valido")

try:
    while True:
        continua = input("Vuoi inserire un altro animale? (s/n): ")
        if continua.lower() != 's':
            break

except Exception as e:
    print(f"Si è verificato un ecezione: {e}")