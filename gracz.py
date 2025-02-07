import collections

class Gracz:
    def __init__(self, nazwa, talia_kart):
        self.nazwa = nazwa
        self.reka = talia_kart.dobierz_karte(5)
        self.uklad = ""
        self.wynik = ""

    def pokaz_karty(self):
        return ", ".join(str(karta.przedstaw_karty()) for karta in self.reka)

    def wymien_karty(self, talia_kart, ktore_karty):
        for karta in ktore_karty:
            self.reka[karta] = talia_kart.dobierz_karte(1)[0]

    def porownanie_kart(self):
        wartosci = []
        kolory = []
        for karta in self.reka:
            wartosci.append(karta.wartosc)
            kolory.append(karta.kolor)
        zmiana_wartosci = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11,
                           'D': 12, 'K': 13, 'A': 14}
        wartosci_liczbowe = sorted([zmiana_wartosci[wartosc] for wartosc in wartosci])
        obliczone_wartosci = collections.Counter(wartosci_liczbowe)
        obliczone_kolory = collections.Counter(kolory)
        if wartosci_liczbowe == [10, 11, 12, 13, 14] and obliczone_kolory.values() == 5:
            self.uklad = "Poker królewski"
            self.wynik = 10
        elif wartosci_liczbowe == [5,6,7,8,9] and obliczone_kolory.values() == 5:
            self.uklad = "Poker"
            self.wynik = 9
        elif 4 in obliczone_wartosci.values():
            self.uklad = "Kareta"
            self.wynik = 8
        elif 3 in obliczone_wartosci.values() and 2 in obliczone_wartosci.values():
            self.uklad = "Full"
            self.wynik = 7
        elif obliczone_kolory.values() == 5:
            self.uklad = "Kolor"
            self.wynik = 6
        elif (wartosci_liczbowe[4] == (wartosci_liczbowe[3]+1) and wartosci_liczbowe[3] == (wartosci_liczbowe[2]+1) and
              wartosci_liczbowe[2] == (wartosci_liczbowe[1]+1)) and wartosci_liczbowe[1] == (wartosci_liczbowe[0]+1):
            self.uklad = "Strit"
            self.wynik = 5
        elif 3 in obliczone_wartosci.values():
            self.uklad = "Trójka"
            self.wynik = 4
        elif list(obliczone_wartosci.values()).count(2) == 2:
            self.uklad = "Dwie Pary"
            self.wynik = 3
        elif 2 in obliczone_wartosci.values():
            self.uklad = "Para"
            self.wynik = 2
        else:
            self.uklad = "Brak układu"
            self.wynik = 1


