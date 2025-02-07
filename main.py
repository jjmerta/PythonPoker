import poker, os

silnik_gry = poker.Poker()
wynik, zapis_wyniku = silnik_gry.gra()
print(wynik)

if os.path.exists("zapis_rozgrywki.txt"):
    os.remove("zapis_rozgrywki.txt")

with open("zapis_rozgrywki.txt", "w", encoding='utf-8') as plik:
    plik.write(zapis_wyniku)



