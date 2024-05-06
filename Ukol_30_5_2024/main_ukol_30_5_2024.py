#Úkol 1
#Uživatel zadá šestimístné číslo. Napište program, který určí, zda je toto číslo šťastné. (Šťastné číslo je šestimístné číslo, jehož součet prvních tří číslic se rovná součtu jeho posledních tří číslic.)
#Například 123321 je šťastné číslo, protože 1+2+3 = 3+2+1.
#Ale 378423 není šťastné číslo, protože 3+7+8 != 4+2+3.
#Pokud uživatel zadal jiné než šestimístné číslo, zobrazí se chybová zpráva.


#Úkol 2
#Uživatel zadá šestimístné číslo. Prohoďte první a šestou číslici a také druhou a pátou.
#Například 723895 by se mělo stát 593827.
#Pokud uživatel zadal jiné než šestimístné číslo, zobrazí se chybová zpráva.

def swap_number(number):
    if len(str(number)) != 6:
        print("Chyba zadej prosím šestimístné číslo. ")
        return None

    #rozdělení čísla
    digits = [int(digit) for digit in str(number)]

    #prohození číslic
    digits[0], digits[5] = digits[5], digits[0] # prohození 1 a 6
    digits[1], digits[4] = digits[4], digits[1]  # prohození 2 a 5

    #vrácení čísla
    swaped_number = int("".join(map(str, digits)))
    return swaped_number

# spustení funkce

#spustit odkomentováním níže:
"""
input_number = int(input("Zadej šestimístné číslo: "))
swapped = swap_number(input_number)
if swapped is not None:
    print("Prohozené číslo: ", swapped)
"""

#Úkol 3
#Uživatel zadá číslo měsíce (od 1 do 12). Na základě zadaného čísla program zobrazí jedno z následujících: Zima, pokud je číslo 1, 2 nebo 12, Jaro, pokud je číslo v rozsahu od 3 do 5, Léto, pokud je od 6 do 8, Podzim, pokud je od 9 až 11.
#Pokud je číslo mimo rozsah, zobrazí se chybová zpráva.

def season(num):
    if num < 1 or num > 12:
        print("Zadal jsi špatné číslo takový měsíc nemáme ")
    elif num in [1, 2, 12]:
        print("Zadal jsi měsíc zima.")
    elif num >= 3 and num <= 5:
        print("Zadal jsi měsíc léta.")
    elif num >= 6 and num <= 8:
        print("Zadal jsi měsíc léta.")
    elif num >= 9 and num <= 11:
        print("Zadal jsi měsíc léta.")

input_season_number = int(input("Zadej číslo měsíce od 1 do 12: "))
season(input_season_number)










