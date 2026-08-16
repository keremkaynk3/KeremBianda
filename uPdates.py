import sqlite3 as sql
import os

# SQLite veritabanı bağlantısı
db_path = os.path.join(os.path.dirname(__file__), "blog.db")
db = sql.connect(db_path)
cursor = db.cursor()

# Fotoğraf verisi
class uPdates():
    def add_Photo(self):
        photo_info = input("Enter a location that photo you want to add...")
        c = input("Which country does it belong that you want to add?")
        with open(f'{photo_info}', 'rb') as file:
            foto_bytes = file.read()
        cursor.execute("UPDATE Countries SET images=? WHERE country_name=?", (foto_bytes, f"{c}"))
        db.commit()
        print("Photo added succesfully!")

    def add_Country(self):
        print("Enter that informations carefully about country that you want to add")
        a = input("Country Name:")
        b = input("Video Link (If not exist press 'ENTER' :")
        c = input("Capital City:")
        d = input("Country Code:")
        e = input("Population:")
        f = input("Currency:")
        g = input("Cities you have ever been:")
        h = 0
        sorgu = "INSERT INTO Countries(country_name, links, capital, country_code, population, currency, cities, images) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sorgu, (a, b, c, d, e, f, g, h))
        db.commit()
        print("Ülke bilgisi veritabanına eklendi...")