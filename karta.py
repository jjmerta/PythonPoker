class Karta:
    def __init__(self, kolor, wartosc):
        self.kolor = kolor
        self.wartosc = wartosc

    def przedstaw_karty(self):
        return f"{self.kolor}{self.wartosc}"

