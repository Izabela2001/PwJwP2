import sqlite3


connection = sqlite3.connect('sales.db')
db = connection.cursor()
#podpunkt a
print("a) Sprzedaż - tylko 'Laptop':")
db.execute("SELECT * FROM sales WHERE product = ?", ('Laptop',))
for record in db.fetchall():
    print(record)
#podpunkt b
print("\nb) Sprzedaż z 2025-05-07 i 2025-05-08:")
selected_dates = ('2025-05-07', '2025-05-08')
db.execute("SELECT * FROM sales WHERE date IN (?, ?)", selected_dates)
for record in db.fetchall():
    print(record)

#podbpukt c
print("\nc) Transakcje z ceną > 200 zł:")
db.execute("SELECT * FROM sales WHERE price > ?", (200,))
for record in db.fetchall():
    print(record)

#podpunkt d
print("\nd) Suma sprzedaży dla każdego produktu:")
db.execute("""
    SELECT product, SUM(quantity * price) AS total_value
    FROM sales
    GROUP BY product
""")
for record in db.fetchall():
    print(record)

#podpunkt e
print("\ne) Dzień z największą liczbą sprzedanych sztuk:")
db.execute("""
    SELECT date, SUM(quantity) AS total_quantity
    FROM sales
    GROUP BY date
    ORDER BY total_quantity DESC
    LIMIT 1
""")
top_day = db.fetchone()
if top_day:
    print(f"{top_day[0]} - {top_day[1]} szt.")


connection.close()