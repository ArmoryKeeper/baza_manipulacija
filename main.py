import sqlite3

## inicijalizacija baze
conn = sqlite3.connect("knjige.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Knjige(
   knjigeId INT PRIMARY KEY,
   ime TEXT,
   godina INT);
""")
conn.commit()

choice = ''
id = 1
while choice!='x':
    choice = input("Baza Knjiga:\nOpcija 1: unos knjige u bazu\nOpcija 2: iscitavanje iz baze\nOpcija x: izlaz\n")

    if choice == '1':

        unos = {"knjigeId":id,"ime":'',"godina":0}
        unos["ime"] = input('Unesite ime knjige: ')
        unos["godina"] = int(input('Unesite godinu izdanja knjige: '))
        cursor.execute("INSERT INTO Knjige VALUES (:knjigeId, :ime, :godina)", unos)
        conn.commit()
        id += 1
    elif choice == '2':
        cursor.execute("SELECT * FROM Knjige;")
        rezultat = cursor.fetchall()
        print(rezultat)
    elif choice == 'x':
        print("Dovidjenja")
    else:
        print('Nepravilan unos')




