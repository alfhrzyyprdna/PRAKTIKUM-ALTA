import sqlite3

connect_to_db = sqlite3.connect("Cars.db")

k = connect_to_db.cursor()
k.execute("""
          Select * From TBCars
          """)

print(k.fetchall())

connect_to_db.close()