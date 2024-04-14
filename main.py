#Úkol:
#Úkol 1:
#Vytvořte základní třídu Shape s metodou pro výpočet plochy. Vytvořte odvozené třídy: obdélník, kruh, pravý trojúhelník, lichoběžník s vlastními metodami pro výpočet plochy.
#Úkol 2
#Přepište metody int (vrací oblast) a str (vrací informace o tvaru) z úkolu 1.
#Úkol 3
#Vytvořte základní třídu Shape pro kreslení plochých tvarů.
#Definujte následující metody:
#- Show() — tisk informací o tvaru;
#- Save() — uložení tvaru do souboru;
#- Load() – čtení tvaru ze souboru.
#Definujte odvozené třídy:
#- Čtverec – čtverec definovaný souřadnicemi horního levý roh a délka strany;
#- Obdélník – obdélník se zadanými souřadnicemi levý horní roh a rozměry;
#Domácí práce
#- Kružnice – kružnice se zadanými souřadnicemi středu a poloměru;
#- Elipsa — elipsa se zadanými souřadnicemi horního rohu opsaného obdélníku, jehož strany jsou rovnoběžné s osami souřadnic a rozměry tohoto obdélníku.
#Vytvořte seznam obrazců, uložte obrazce do souboru, načtěte je do jiného seznamu a zobrazte informace o každém obrazci.


from Shapes import Shape,Rectangle, Circle, RightTriangle

# Vytvoření seznamu tvarů
shapes = [
    Rectangle(10, 5),
    Circle(7),
    RightTriangle(3, 4)
]

#uložení do souboru
for index, shape in enumerate(shapes):
    shape.Save(f"shapes/{index}.txt")

#načtení tvarů
loaded_shapes = []
for index in range(len(shapes)):
    loaded_shape = Shape.Load(f"shapes/{index}.txt")
    loaded_shapes.append(loaded_shape)

#zobrzaení infomací o tvaru
for shape in loaded_shapes:
    shape.Show()



