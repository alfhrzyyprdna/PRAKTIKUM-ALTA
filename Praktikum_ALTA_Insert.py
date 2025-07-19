import sqlite3

connect_to_db = sqlite3.connect("Cars.db")

k = connect_to_db.cursor()

k.execute("""
    INSERT INTO TBCars (
        id,
        name,
        brand,
        model,
        price
    )
    VALUES 
        ('104', 'BMW', 'Luxury Car', 'M4', 20000),
        ('105', 'Porsche', 'Sport Car', '911 gt3 rs', 15000)
""")


connect_to_db.commit()
connect_to_db.close()