import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='Animali'
)
mycursor = mydb.cursor()


def insert_initial_animals():
    sql = f"INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    val = [
        ('Fido', 'Labrador', 30, 5),
        ('Kitty', 'Siamese', 4, 2),
        ('Leo', 'Leone', 190, 8),
        ('Dumbo', 'Elefante', 5000, 15),
        ('Speedy', 'Ghepardo', 55, 3)
    ]
    mycursor.executemany(sql, val)
    mydb.commit()

def display_all_animals():
    mycursor.execute(f"SELECT Id, Nome_Proprio, Razza, Peso, Eta FROM Mammiferi")
    records = mycursor.fetchall()

    if not records:
        print("\nNessun animale trovato nel database.")
        return
    print("\n--- Tutti gli Animali nel Database ---")
    for row in records:
        print(row)
    print("---------------------------------------")


def get_animal_data():
    nome = input("Nome: ")
    razza = input("Razza: ")
    peso = int(input("Peso (intero): "))
    eta = int(input("Età (intero): "))
    return (nome, razza, peso, eta)

def insert_single_animal():
    sql = f"INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    print("\nInserisci i dati per il nuovo animale:")
    animal_data = get_animal_data()
    mycursor.execute(sql, animal_data)
    mydb.commit()
    print("Animale inserito.")

def delete_animal_by_id():
    animal_id = int(input("Inserisci l'ID dell'animale da eliminare: "))
    sql = f"DELETE FROM Mammiferi WHERE Id = %s"
    mycursor.execute(sql, (animal_id,))
    mydb.commit()
    if mycursor.rowcount > 0:
        print(f"Animale con ID {animal_id} eliminato con successo.")
    else:
        print(f"Nessun animale trovato con ID {animal_id}.")

def update_animal_by_id():
    animal_id = int(input("Inserisci l'ID dell'animale da modificare: "))
    mycursor.execute(f"SELECT * FROM Mammiferi WHERE Id = %s", (animal_id,))
    existing_animal = mycursor.fetchone()
    if not existing_animal:
        print(f"Nessun animale trovato con ID {animal_id}.")
        return

    print(f"\n--- Modifica animale con ID: {animal_id} ---")
    print("Reinserisci tutti i nuovi dati per l'animale:")
    animal_data = get_animal_data()
    sql = f"UPDATE Mammiferi SET Nome_Proprio = %s, Razza = %s, Peso = %s, Eta = %s WHERE Id = %s"
    mycursor.execute(sql, (animal_data[0], animal_data[1], animal_data[2], animal_data[3], animal_id))
    mydb.commit()
    if mycursor.rowcount > 0:
        print(f"Animale con ID {animal_id} modificato con successo.")
    else:
        print(f"Nessuna modifica effettuata per l'animale con ID {animal_id}.")

def main_menu():
    insert_initial_animals()
    display_all_animals()

    while True:
        print("\n--- MENU GESTIONE ANIMALI ---")
        print("1. Inserisci un nuovo animale")
        print("2. Visualizza tutti gli animali")
        print("3. Elimina un animale (per ID)")
        print("4. Modifica un animale (per ID)")
        print("5. Esci")

        choice = input("Inserisci la tua scelta: ")

        if choice == '1':
            insert_single_animal()
        elif choice == '2':
            display_all_animals()
        elif choice == '3':
            delete_animal_by_id()
        elif choice == '4':
            update_animal_by_id()
        elif choice == '5':
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main_menu()