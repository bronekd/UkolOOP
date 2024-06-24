import sqlite3
import csv

def load_csv_to_db(filename, table_name, conn):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames
        cursor = conn.cursor()

        for row in reader:
            values = [row[column] for column in columns]
            placeholders = ', '.join(['?'] * len(columns))
            query = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({placeholders})'
            cursor.execute(query, values)
        conn.commit()

def main():
    conn = sqlite3.connect('sales.db')

    # Vymazání dat z tabulek před načtením nových dat
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Salespeople')
    cursor.execute('DELETE FROM Customers')
    cursor.execute('DELETE FROM Sale')
    conn.commit()

    # Načítání dat do tabulek
    load_csv_to_db('salespeople.csv', 'Salespeople', conn)
    load_csv_to_db('customers.csv', 'Customers', conn)
    load_csv_to_db('sales.csv', 'Sale', conn)  # Ujistěte se, že název tabulky je správný ('Sale')

    conn.close()
    print('Data nahrána do db')

if __name__ == "__main__":
    main()
