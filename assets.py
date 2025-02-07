tytul = r'''
 ____        _   _                   ____       _             
|  _ \ _   _| |_| |__   ___  _ __   |  _ \ ___ | | _____ _ __ 
| |_) | | | | __| '_ \ / _ \| '_ \  | |_) / _ \| |/ / _ \ '__|
|  __/| |_| | |_| | | | (_) | | | | |  __/ (_) |   <  __/ |   
|_|    \__, |\__|_| |_|\___/|_| |_| |_|   \___/|_|\_\___|_|   
       |___/   
'''
wstep = "♥♦     Witaj w grze Python Poker!     ♠♣"
instrukcja = '''Gra polega na rozdaniu każdemu graczowi pięciu kart, a następnie porównaniu układów, aby wyłonić zwycięzcę. 
W grze bierze udział użytkownik oraz trzech komputerowych przeciwników.

Przebieg gry:
1. Każdy z graczy otrzymuje pięć losowych kart z przetasowanej talii.
2. Gracz ma możliwość oceny swojego układu.
3. Po rozdaniu i analizie kart następuje porównanie rąk graczy.
4. Wygrywa ten, kto ma najwyższy układ według zasad pokera

Zasady pokera:
Poker królewski – A, K, Q, J, 10 w tym samym kolorze.
Poker – Pięć kolejnych kart w tym samym kolorze (np. 5♠-6♠-7♠-8♠-9♠).
Kareta – Cztery karty o tej samej wartości (np. K-K-K-K-7).
Full – Trójka i para (np. 10-10-10-7-7).
Kolor – Pięć kart w tym samym kolorze, ale nie po kolei (np. 2♣-5♣-9♣-J♣-K♣).
Strit – Pięć kolejnych kart w różnych kolorach (np. 4-5-6-7-8).
Trójka – Trzy karty o tej samej wartości (np. Q-Q-Q-5-2).
Dwie pary – Dwie różne pary (np. 9-9-5-5-J).
Para – Dwie karty o tej samej wartości (np. A-A-3-7-9).
'''