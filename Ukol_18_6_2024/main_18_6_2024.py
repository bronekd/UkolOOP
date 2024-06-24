import sqlite3


def show_menu():
    print("Welcome to")
    print("Menu:")
    print("1. Zobrazit všechny nákupy")
    print("2. Zobrazit nákupy od konkrétního prodejce")
    print("3. Zobrazit největší množství prodejů")
    print("4. Zobrazit nejmenší množství prodejů")
    print("5. Zobrazit největší množství prodejů pro konkrétního prodejce")
    print("6. Zobrazit nejmenší množství prodejů pro konkrétního prodejce")
    print("7. Zobrazit největší nákup konkrétního zákazníka")
    print("8. Zobrazit nejmenší nákup konkrétního zákazníka")
    print("9. Zobrazit prodejce s největším množstvím prodejů")
    print("10. Zobrazit zákazníka s největším nákupem")
    print("0. Ukončit")

def get_sales_data(query, params=None):
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

def display_all_purchases():
    data = get_sales_data("SELECT * FROM Sale")
    for row in data:
        print(row)

def display_purchases_by_salesperson(salesperson_id):
    data = get_sales_data("SELECT * FROM Sale WHERE Salesperson_id = ?", (salesperson_id,))
    for row in data:
        print(row)


def display_max_sales():
    data = get_sales_data("SELECT MAX(amount) FROM Sale")
    print(data[0][0])

def display_min_sales():
    data = get_sales_data("SELECT MIN(amount) FROM Sale")
    print(data[0][0])

def display_max_sales_by_salesperson(salesperson_id):
    data = get_sales_data("SELECT MAX(amount) FROM Sale WHERE salesperson_id = ?", (salesperson_id,))
    print(data[0][0])

def display_min_sales_by_salesperson(salesperson_id):
    data = get_sales_data("SELECT MIN(amount) FROM Sale WHERE salesperson_id = ?", (salesperson_id,))
    print(data[0][0])

def display_max_purchase_by_customer(customer_id):
    data = get_sales_data("SELECT MAX(amount) FROM Sale WHERE customer_id = ?", (customer_id,))
    print(data[0][0])

def display_min_purchase_by_customer(customer_id):
    data = get_sales_data("SELECT MIN(amount) FROM Sale WHERE customer_id = ?", (customer_id,))
    print(data[0][0])

def display_salesperson_with_max_sales():
    data = get_sales_data("""
        SELECT Salespeople.name, SUM(Sale.amount) as total_sale
        FROM Sale
        JOIN Salespeople ON Sale.salesperson_id = Salespeople.id
        GROUP BY Sale.salesperson_id
        ORDER BY total_sale DESC
        LIMIT 1
    """)
    print(data[0][0], data[0][1])

def display_customer_with_max_purchase():
    data = get_sales_data("""
        SELECT Customers.name, SUM(Sale.amount) as total_purchase
        FROM Sale
        JOIN Customers ON Sale.customer_id = Customers.id
        GROUP BY Sale.customer_id
        ORDER BY total_purchase DESC
        LIMIT 1
    """)
    print(data[0][0], data[0][1])


def main():
    while True:
        show_menu()
        choice = input("Vyberte možnost: ")
        if choice == "1":
            display_all_purchases()
        elif choice == "2":
            salesperson_id = int(input("Zadej ID prodejce: "))
            display_purchases_by_salesperson(salesperson_id)
        elif choice == "3":
            display_max_sales()
        elif choice == "4":
            display_min_sales()
        elif choice == "5":
            salesperson_id = int(input("Zadejte ID prodejce: "))
            display_max_sales_by_salesperson(salesperson_id)
        elif choice == "6":
            salesperson_id = int(input("Zadejte ID prodejce: "))
            display_min_sales_by_salesperson(salesperson_id)
        elif choice == "7":
            customer_id = int(input("Zadejte ID zákazníka: "))
            display_max_purchase_by_customer(customer_id)
        elif choice == "8":
            customer_id = int(input("Zadejte ID zákazníka: "))
            display_min_purchase_by_customer(customer_id)
        elif choice == "9":
            display_salesperson_with_max_sales()
        elif choice == "10":
            display_customer_with_max_purchase()
        elif choice == ("0"):
            break
        else:
            print("Neplatná volba, zkuste to znovu")

if __name__ == "__main__":
    main()



