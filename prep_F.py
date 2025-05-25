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
except mysql.connector.Error as errore:
    print(f"Errore: {errore}")
except Exception as ecezione:
    print(f"Si è verificato un ecezione: {ecezione}")

try:
    while True:
        print("\nInserisci i dati per il nuovo animale:")
        nome = input("Nome: ")
        razza = input("Razza: ")
        peso_str = input("Peso (intero): ")
        eta_str = input("Età (intero): ")

        try:
            peso = int(peso_str)
            eta = int(eta_str)
            val = (nome, razza, peso, eta)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Animale inserito con successo.")
        except ValueError:
            print("Errore: Peso ed Età devono essere numeri interi. Riprova.")
            continue
        except mysql.connector.Error as err:
            print(f"Errore durante l'inserimento: {err}")

        continua = input("Vuoi inserire un altro animale? (s/n): ")
        if continua.lower() != 's':
            break

except Exception as e:
    print(f"Si è verificato un ecezione: {e}")