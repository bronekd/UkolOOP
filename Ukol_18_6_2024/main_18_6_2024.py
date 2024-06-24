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

def main():
    while True:
        show_menu()
        choice = input("Vyberte možnost: ")
        if choice == "1":
            display_all_purchases()
        elif choice == "2":
            salesperson_id = int(input("Zadej ID prodejce: "))
            display_purchases_by_salesperson(salesperson_id)
        elif choice == ("0"):
            break
        else:
            print("Neplatná volba, zkuste to znovu")

if __name__ == "__main__":
    main()



