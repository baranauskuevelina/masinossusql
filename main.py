import sqlite3


def create_table():
    conn = sqlite3.connect("masinos.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS automobiliai (
                id INTEGER PRIMARY KEY,
                marke TEXT,
                modelis TEXT,
                spalva TEXT,
                metai INTEGER,
                kaina REAL
            )""")
    conn.commit()
    conn.close()


def save_to_db(marke, modelis, spalva, metai, kaina):
    conn = sqlite3.connect("masinos.db")
    c = conn.cursor()
    c.execute("INSERT INTO automobiliai (marke, modelis, spalva, metai, kaina) VALUES (?, ?, ?, ?, ?)",
              (marke, modelis, spalva, metai, kaina))
    conn.commit()
    conn.close()


def search_in_db(marke, modelis, spalva, metai_nuo, metai_iki, kaina_nuo, kaina_iki):
    conn = sqlite3.connect("masinos.db")
    c = conn.cursor()
    paieska = """SELECT * FROM automobiliai
                 WHERE marke LIKE ?
                 AND modelis LIKE ?
                 AND spalva LIKE ?
                 AND metai BETWEEN ? AND ?
                 AND kaina BETWEEN ? AND ?"""
    c.execute(paieska, (marke, modelis, spalva, metai_nuo, metai_iki, kaina_nuo, kaina_iki))
    results = c.fetchall()
    conn.close()
    return results


def display_all():
    conn = sqlite3.connect("masinos.db")
    c = conn.cursor()
    c.execute("SELECT * FROM automobiliai")
    results = c.fetchall()
    conn.close()
    return results


# Create the table if it doesn't exist
create_table()

while True:
    pasirinkimas = int(input("1 - įvesti automobilį\n2 - paieška\n3 - atvaizduoti automobilius\n0 - išeiti\n"))

    if pasirinkimas == 1:
        print("Įveskite automobilį:")
        marke = input("Markė: ")
        modelis = input("Modelis: ")
        spalva = input("Spalva: ")
        metai = int(input("Metai: "))
        kaina = float(input("Kaina: "))
        save_to_db(marke, modelis, spalva, metai, kaina)

    elif pasirinkimas == 2:
        marke = input("Markė: ") + "%"
        modelis = input("Modelis: ") + "%"
        spalva = input("Spalva: ") + "%"
        metai_nuo = input("Metai nuo: ")
        metai_nuo = int(metai_nuo) if metai_nuo else 1900
        metai_iki = input("Metai iki: ")
        metai_iki = int(metai_iki) if metai_iki else 2100
        kaina_nuo = input("Kaina nuo: ")
        kaina_nuo = float(kaina_nuo) if kaina_nuo else 0
        kaina_iki = input("Kaina iki: ")
        kaina_iki = float(kaina_iki) if kaina_iki else 10000000
        results = search_in_db(marke, modelis, spalva, metai_nuo, metai_iki, kaina_nuo, kaina_iki)
        print(results)

    elif pasirinkimas == 3:
        results = display_all()
        print(results)

    elif pasirinkimas == 0:
        print("Viso gero")
        break
