## Instrukcja instalacji:

1. Utwórz venv (albo i nie ;))
2. `pip install -r requirements.txt`

## Zadania warsztatowe
Do wykonania grupowo (3 osoby na grupę)

### Zadanie 1 - moduł palindrome
*Palindrom - wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej.*

1. Napisz funkcję is_palindrome która sprawdzi czy wyraz jest palindromem
2. Napisz test który potwierdzi, że pojedyńcze słowa **są** palindromami (`abba`, `sedes`, `Potop`)
3. Napisz test który potwierdzi, że następujące słowa **nie są** palindromami (`albicla`, `radar`)
4. Rozbuduj funkcję is_palindrome tak żeby sprawdzała również zdania (spacje się nie liczą).
5. Przykłady palindromów do testowania (`A warta kosy wysoka trawa`, `Zakopane i nie na pokaz`)
6. Napisz testy dla zdań które są palindromami, oraz takich które nimi nie są (pamiętaj o przypadkach negatywnych).
7. Rozbuduj funkcję `is_palindrome` tak żeby omijał znaki specjalne. Tzn. następujące stringi też są palindromami (`Ilu beczy z cebuli?`, `O, i natka tu tak tanio!`)
8. Sprawdź pokrycie kodem metody `is_palindrome`. Spróbuj dobić do 100 procent.

### Zadanie 2 - moduł badcode
W pliku `pesel.py` znajduje się błędna funkcja `analyze_pesel()`. Funkcja ta przyjmuje jeden parametr: `pesel`, a zwraca słownik z następującymi kluczami:

    "pesel": wejściowy numer,
    "gender": płeć zakodowaną w numerze (male / female),
    "birth_date": datę urodzenia zakodowaną w numerze,
    "valid": czy numer jest poprawny.

Napisz testy jednostkowe, które sprawdzą:
- czy funkcja poprawnie waliduje numer pesel, 
- czy funkcja zwraca poprawne dane.
 
Pamiętaj, by przetestować numery osób urodzonych po 31 grudnia 1999 roku.
Popraw ewentualne błędy, aż wszystkie napisane przed chwilą testy przejdą.

Dla generowania poprawnych peseli możesz użyć strony [generator peseli](http://pesel.felis-net.com/)


### Zadanie 3 - moduł badcode
W pliku `answer.py` znajduje się funkcja `is_this_answer_to_ultimate_question_of_life(n):` napisana przez średnio poczytalnego programistę Pythona.
Napisz test, który sprawdzi czy wszystkie przypadki `n` od 1 do 100 włącznie **nie zwracają** napisu `"That should not happen at all!"`

### Zadanie 4 - moduł goodcode
W pliku `htmlformatter.py` jest klasa z różnymi funkcjami. Pokryj 100% kodu testami jednostkowymi.


### Zadanie 5 - moduł goodcode
W pliku `logstream.py` jest aplikacja która po uruchomieniu będzie wyrzucać logi na stdout.
Zastanówcie się jak ją przetestować. Czy warto ją zrefaktoryzować? Testowanie stdout może być problematyczne.
Jakie testy powinniśmy napisać zakładając, że te logi są parsowane i generujemy z nich dashboardy?