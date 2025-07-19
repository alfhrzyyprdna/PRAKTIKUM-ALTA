import sqlite3

connect_to_db = sqlite3.connect("Cars.db")

k = connect_to_db.cursor()

k.execute("""
          Update TBCars Set
          price = 30000
          where
          id = 104
          """)
print(k.fetchall())

connect_to_db.commit()
connect_to_db.close()