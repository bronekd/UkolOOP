# třída Device
class Device:
    def __init__(self, name, vyrobce = None, rok_vyroby = None):
        self.name = name
        self.vyrobce = vyrobce
        self.rok_vyroby = rok_vyroby
    def typ_device(self):
        print(f"Device Jméno: {name}, Výrobce: {vyrobce}, Rok výroby: {rok_vyroby}")