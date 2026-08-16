import sqlite3 as sql
import os

db_path = os.path.join(os.path.dirname(__file__), "blog.db")
db = sql.connect(db_path)
cursor = db.cursor()


db.commit()
db.close()

print("Data inserted successfully.")

