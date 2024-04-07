# Úkol
# Úkol 1
#Vytvořte třídu Device obsahující informace o zařízení. Pomocí dědičnosti implementujte třídu CoffeeMachine (obsahuje informace o kávovaru), třídu Blender (obsahuje informace o mixéru), třídu MeatGrinder (obsahuje informace o mlýnku na maso).
# # Každá třída musí mít požadované metody.
# Úkol 2
# Vytvořte třídu Loď obsahující informace o lodi. Použijte dědičnost k implementaci třídy Fregata (obsahuje informace o fregatě), třídy Destroyer (obsahuje informace o torpédoborci), třídy Cruiser (obsahuje informace o křižníku). Každá třída musí mít požadované metody.
# Úkol 3
# Vytvořte třídu Money pro práci s penězi (objekt třídy pracuje s jednou měnou). Třída musí poskytovat pole pro uložení celé části (dolary, eura, hřivny atd.) a pole pro uložení zlomkové části (centy, eurocenty, kopejky atd.) Implementujte metody pro tisk množství a nastavení hodnot pro díly (celé číslo a zlomky).
#Na základě třídy Money vytvořte třídu Product. Implementujte metodu, která vám umožní snížit cenu o zadané číslo.
#Implementujte metody a pole požadované pro každou třídu.

from Device import Device
from CoffeeMachine import CoffeeMachine
from Blender import Blender
from MeatGrinder import MeatGrinder

my_device = Device("Tiskárna", "Cannon", 2016)
my_device.typ_device()
print()

my_coffee_machine = CoffeeMachine("Kávovar Delux", "Caffe Master", 2020, 200, "Lungo")
my_coffee_machine.priprav_kavu()
my_coffee_machine.zobraz_info()
print()

my_blender = Blender("Mixér Mix Vše", "Sencor", "2021", 2000, 5)
my_blender.zobraz_info()
my_blender.mixuj()
print()

my_meat_grinder = MeatGrinder("Mlýnek Melu vše", "Rowenta", "2021", 2000, 2)
my_meat_grinder.mleti()
my_meat_grinder.zmena_nozu(5)
my_meat_grinder.mleti()