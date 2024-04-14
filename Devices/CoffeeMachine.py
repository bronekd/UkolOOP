from Device import Device


class CoffeeMachine(Device):
    def __init__(self, name, vyrobce, rok_vyroby, objem_nadoby, typ_kavy = None):
        super().__init__(name, vyrobce, rok_vyroby)
        self.objem_nadoby = objem_nadoby
        self.typ_kavy = typ_kavy
    def priprav_kavu(self):
        if self.typ_kavy:
            print(f"Příprava kavu: {self.typ_kavy}")
        else:
            print("Příprava běžné kávy")
    def zobraz_info(self):
        super().typ_device() #zobrazí obecné informace z Device
        print(f"Objem nádoby: {self.objem_nadoby}, typ kavy: {self.typ_kavy if self.typ_kavy else 'Všechny typy'}")


