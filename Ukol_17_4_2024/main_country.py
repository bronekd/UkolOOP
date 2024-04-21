import json

countries_capitals = {}

# přidání země a města do slovníku:
def add_country(country, capital):
    countries_capitals[country] = capital

#Odstranění země ze slovníku
def delete_country(country):
    if country in countries_capitals:
        del countries_capitals[country]
    else:
        print(f"{country} nenalezeno. ")

#Hledání hlavního města
def find_capital(country):
    if country in countries_capitals:
        return countries_capitals[country]
    else:
        return f"{country} nenalezeno. "

#editace hlavního města
def edit_country(country, new_capital):
    if country in countries_capitals:
        countries_capitals[country] = new_capital
    else:
        print(f"{country} nenalezeno. ")

#Uložení do souboru
def save_data(filename):
    with open(filename, 'w') as file:
        json.dump(countries_capitals, file)

# načtení dat ze souboru
def load_data(filename):
    global countries_capitals
    with open(filename, 'r') as file:
        countries_capitals = json.load(file)


#použití funkcí
add_country("Cesko", "Praha")
add_country("Slovensko", "Bratislava")
add_country("Nemecko", "Berlin")

#vypsat slovník
print(f"Vypsání vytvořeného dlovníku: {countries_capitals}")
print()

#Editace
edit_country("Slovensko", "Kosice")
print(f"Editace Slovenska: {countries_capitals}")
print()

#smazání dat
delete_country("Nemecko")
print(f"Smazání Nemecka: {countries_capitals}")
print()

#uložení dat
save_data("countries_capitals.json")
print("Data byla uložena do souboru countries_capitals.json")
print()

#umělé vymazání dat ze slovníku
countries_capitals = {}
print(f"Vymazaný slovník: {countries_capitals}")

#Opětovné načtení dat
load_data("countries_capitals.json")
print(f"Opětovně načtený slovník: {countries_capitals}")

