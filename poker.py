import talia,gracz,assets
import time

class Poker:
    def __init__(self):
        self.talia = talia.Talia()
        self.komp1 = gracz.Gracz("Komputer 1", self.talia)
        self.komp2 = gracz.Gracz("Komputer 2", self.talia)
        self.komp3 = gracz.Gracz("Komputer 3", self.talia)
        self.gracz = gracz.Gracz("Gracz", self.talia)

    def gra(self):
        print(assets.tytul)
        print(assets.wstep)

        pomoc = input("Wpisz 'help' jeśli chcesz przeczytać instrukcję. \nNaciśnij enter aby rozpocząć rozgrywkę: \n")
        if pomoc.lower() == "help":
            print(assets.instrukcja)
            input("Naciśnij enter aby rozpocząć rozgrywkę: \n")

        self.gracz.porownanie_kart()
        print(f"Twoje karty: {self.gracz.pokaz_karty()}. Układ: {self.gracz.uklad}")
        zmiana_kart = input("Podaj numer karty, którą chcesz wymienić. Naciśnij enter aby pominąć: \n")

        if zmiana_kart:
            zmieniane_karty = []
            for numer in zmiana_kart.split():
                zmieniane_karty.append(int(numer)-1)
            self.gracz.wymien_karty(self.talia,zmieniane_karty)
            print(f"Karty po wymianie: {self.gracz.pokaz_karty()}. Układ: {self.gracz.uklad}")
            input("Kliknij enter aby odkryć karty: \n")

        self.komp1.porownanie_kart()
        self.komp2.porownanie_kart()
        self.komp3.porownanie_kart()

        talia_gracz = f"Karty po wymianie {self.gracz.pokaz_karty()}."
        komputer1 = f"Karty Komputer 1: {self.komp1.pokaz_karty()}. Układ: {self.komp1.uklad}."
        komputer2 = f"Karty Komputer 2: {self.komp2.pokaz_karty()}. Układ: {self.komp2.uklad}."
        komputer3 = f"Karty Komputer 3: {self.komp3.pokaz_karty()}. Układ: {self.komp3.uklad}."

        print(komputer1)
        time.sleep(1)
        print(komputer2)
        time.sleep(1)
        print(komputer3)
        time.sleep(1)

        self.gracz.porownanie_kart()

        gracze = {self.komp1: self.komp1.wynik, self.komp2: self.komp2.wynik, self.komp3: self.komp3.wynik,
                  self.gracz: self.gracz.wynik}
        najwyzszy_wynik = max(gracze.values())
        if list(gracze.values()).count(najwyzszy_wynik) > 1:
            wynik = "Mamy remis! Zagraj jeszcze raz!"
        else:
            wygrany = list(gracze.keys())[list(gracze.values()).index(najwyzszy_wynik)]
            wynik = f"Wygrał {wygrany.nazwa} z układem {wygrany.uklad}! Gratulacje!"

        zapis_wynikow = f"{talia_gracz}\n{komputer1}\n{komputer2}\n{komputer3}\n{wynik}"
        return wynik, zapis_wynikow

