from Device import Device

class MeatGrinder(Device):
    def __init__(self, name, vyrobce, rok_vyroby, vykon_motoru, pocet_nozu):
        super().__init__(name, vyrobce, rok_vyroby)
        self.vykon_motoru = vykon_motoru
        self.pocet_nozu = pocet_nozu

    def mleti(self):
        if self.pocet_nozu >1:
            print(f"{self.name} mele maso počtem nožů {self.pocet_nozu}")
        else:
            print(f"{self.name} nemele maso bez nožů")

    def zmena_nozu(self, novy_pocet_nozu):
        self.pocet_nozu = novy_pocet_nozu
        print(f"Počet nožů byl změnen na '{novy_pocet_nozu}' pro {self.name}.")

