# PythonPoker
> **Praca zaliczeniowa - Programowanie w Python**\
> Jakub Merta\
> informatyka niestacjonarna\
> V semestr, spec. AMIPI

## Opis aplikacji:
Do przygotowania projektu wykorzystano programowanie obiektowe uwzględniające klasy i funkcję oraz wykorzystano możliwość zapisywania wyników programu do pliku.

### Budowa aplikacji:
- assets.py (plik zawierający logo aplikacji, tekst instrukcji)
- gracz.py (klasa Gracz)
- karta.py (klasa Karta)
- main.py (główny plik uruchamiający aplikację)
- poker.py (klasa Poker)
- talia.py (klasa Talia)          
- zapis_rozgrywki.txt (plik do wprowadzania wyników rozgrywki)


## Instrukcja obsługi:
Gra polega na rozdaniu każdemu graczowi pięciu kart, a następnie porównaniu układów, aby wyłonić zwycięzcę. 
W grze bierze udział użytkownik oraz trzech komputerowych przeciwników.

### Przebieg gry:
**1.** Każdy z graczy otrzymuje pięć losowych kart z przetasowanej talii.
**2.** Gracz ma możliwość oceny swojego układu.
**3.** Po rozdaniu i analizie kart następuje porównanie rąk graczy.
**4.** Wygrywa ten, kto ma najwyższy układ według zasad pokera

### Zasady pokera:
- **Poker królewski** – A, K, Q, J, 10 w tym samym kolorze.
- **Poker** – Pięć kolejnych kart w tym samym kolorze (np. 5♠-6♠-7♠-8♠-9♠).
- **Kareta** – Cztery karty o tej samej wartości (np. K-K-K-K-7).
- **Full** – Trójka i para (np. 10-10-10-7-7).
- **Kolor** – Pięć kart w tym samym kolorze, ale nie po kolei (np. 2♣-5♣-9♣-J♣-K♣).
- **Strit** – Pięć kolejnych kart w różnych kolorach (np. 4-5-6-7-8).
- **Trójka** – Trzy karty o tej samej wartości (np. Q-Q-Q-5-2).
- **Dwie pary** – Dwie różne pary (np. 9-9-5-5-J).
- **Para** – Dwie karty o tej samej wartości (np. A-A-3-7-9).
