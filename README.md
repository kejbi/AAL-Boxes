# AAL-Boxes, Kacper Biegajski ISI
University Project - AAL Boxes

## Problem
Ortodoksyjny kolekcjoner kartonów zaczyna narzekać na brak miejca. Postanowił oszczędzić miejsce przez wkładanie kartonów jeden w drugi.
W trosce o zachowanie dobrego stanu kartonów wkłada tylko jeden karton wewnątrz większego, a wolną przestrzeń wypełnia materiałem ochronnym.
Tak zabezpieczony karton umieszcza wewnątrz innego większego kartonu. Nie może schować 2 kartonów obok siebie w innym kartonie.
Dla danego zbioru kartonów znaleźć najlepsze upakowanie, czyli zwalniające najwięcej miejsca.

## Algorytm
1. Sortujemy kartony po ich objętości od największego do najmniejszego.
2. Bierzemy największy dostępny karton, traktujemy go jako aktywny, wkładamy jako pierwszy element stosu i usuwamy z listy kartonów.
3. Przechodzimy na następny w kolejności kartonu.
4. Jeżeli dany karton mieści się w aktywnym kartonie, czyli ma wszystkie krawędzie mniejsze, to wkładamy go jako kolejny element stosu,
traktujemy jako aktywny i usuwamy z listy kartonów.
5. Powtarzamy punkty 3 i 4 aż dojdziemy do końca tablicy.
6. Zamykamy stos.
7. Jeżeli lista kartonów nie jest pusta to wracamy do pkt. 2.
8. Zapisane stosy tworzą optymalne upakowanie kartonów.

## Szczegóły implementacyjne (język Python)
- karton reprezentowany jako tuple (x, y, z, V)
- kartony są obracane do postaci x >= y >= z
- wymiary kartonów są typu float
- zbiór kartonów przechowywany jako lista
- stos kartonów przechowywany jako lista

## Plik z danymi wejściowymi
- jedna linia = jeden karton
- 3 współrzędne podane po przecinkach bez spacji, przykład: 3.5,2.0,4.2

## Moduły programu
1. data - wczytywanie danych z plików oraz generacja danych
2. solution - algorytm i pomocnicze funkcje
3. modes - tryby dzialania programu
4. test - testy jednostkowe (biblioteka unitttest)

## Uruchomienie programu
python run.py [-h] [-m1 M1] [-m2 M2] [-m3] [-n N] [-mr MR] [-k K] [-step STEP]
              [-r R]


- -h, --help    pomoc
-   -m1 M1      podaj nazwę pliku wejściowego, rozwiązuje instancję problemu i zwraca plik wyjściowy
-   -m2 M2      podaj nazwę pliku wejściowego, generuje i rozwiązuje instancję problemu oraz zwraca plik wyjściowy (flagi -n i -mr wymagane)
-   -m3         podaj nazwe pliku wyjsciowego, pomiar czasow dla różnych wielkości instancji problemów (-n -k -step -r
               wymagane)
-   -m4         tryb porownania 3 algorytmow
-   -n N        rozmiar instancji problemu
-   -mr MR      max długośc krawędzi kartonu
-   -k K        ilość badanych wielkości instancji (m3)
-   -step STEP  krok (m3)
-   -r R        liczba testów dla każdej wielkości instancji (m3)

#### Przykładowe użycie:
python run.py -m3 -n 1000 -k 19 -step 1000 -r 5

## WE/WY
1. tryb m1 - wejście nazwa pliku wejściowego (txt), wyjście - plik tekstowy o nazwie pliku wejściowego z przedrostkiem output_ z 
intuicyjną reprezentacją upakowania kartonów (każda lista oznacza kolejno upakowane w siebie kartony od największego do najmniejszego, każdy stos kartonów jest oddzielany kreską) i całkowitą objętością
2. tryb m2 - wejście nazwa pliku wyjściowego, wielkość generowanego problemu, max zakres długości krawędzi; wyjście - plik tekstowy o nazwie wprowadzonej na wejściu z upakowanymi kartonami (jak w m1)
3. tryb m3 - wejście nazwa pilku wyjściowego, wielkość początkowej instancji problemu, ilość kroków, rozmiar kroku, liczba testów dla każdej wielkości; wyjście - plik time_test_results.txt z wynikami pomiarów czasowych

## Generowanie instancji problemu
1. Normalne - wartość każdej krawędzi (x, y, z) jest losowana z przedziału od 1 do mr (podanego przez użytkownika) i dodawana jest do niej losowa liczba typu float z przedziału (0,1)
2. Trudne - wartości krawędzi x i y są losowane z przedziału od 1 do 10, krawędź z jest równa z prawdopodobieństwem 92% 0.643, w przeciwnym razie jest równa 0.487. Ma to za zadanie lekko urozmaicić dane, by za każdym razem z nie był ten sam. Częste powtarzanie się jednej z krawędzi zapewnia, że kartony nie będą się w sobie mieścić, co sprawi dla każdego kartonu wiele operacji porównania z innymi. 

### Uruchomienie testów
python -m test.nazwa_pliku_testowego_bez_rozszerzenia

#### Przykład
python -m test.solver_test
