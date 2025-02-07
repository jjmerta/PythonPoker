import random, karta

class Talia:
    def __init__(self):
        wartosci = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "D", "K", "A"]
        kolory = ["♠ ", "♦ ", "♣ ", "♥ "]
        self.karty = []
        for kolor in kolory:
            for wartosc in wartosci:
                self.karty.append(karta.Karta(kolor,wartosc))
        random.shuffle(self.karty)

    def dobierz_karte(self, ile_kart):
        reka = self.karty[:ile_kart]
        self.karty = self.karty[ile_kart:]
        return reka