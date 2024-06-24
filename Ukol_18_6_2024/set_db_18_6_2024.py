#Nastavení databáze
# To znamená vytvoření základních tabulek

import sqlite3

#spojení s db
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

#tvorba tabulek
cursor.execute('''CREATE TABLE IF NOT EXISTS Salespeople (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL)
    ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
    id INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Sale (
    id INTEGER PRIMARY KEY,
    amount REAL NOT NULL,
    salesperson_id INTEGER,
    customer_id INTEGER,
    FOREIGN KEY(customer_id) REFERENCES Customers(id),
    FOREIGN KEY(salesperson_id) REFERENCES Salespeople(id)
)''')


#uložení změn a uzavření spojení
conn.commit()
conn.close()


