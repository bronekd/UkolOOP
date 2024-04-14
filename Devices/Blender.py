from Device import Device

class Blender(Device):
    def __init__(self, name, vyrobce, rok_vyroby, vykon_motoru, objem_nadoby):
        super(). __init__(name, vyrobce, rok_vyroby)
        self.vykon_motoru = vykon_motoru
        self.objem_nadoby = objem_nadoby

    def mixuj(self):
        print(f"Mixér s názvem: {self.name}, mixuje výkonem {self.vykon_motoru} W")

    def zobraz_info(self):
        super().typ_device()
        print(f"Výkon motoru: {self.vykon_motoru}, Objem nádoby: {self.objem_nadoby}")