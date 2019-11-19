# AAL-Boxes, Kacper Biegajski
University Project - AAL Boxes

## Problem
Ortodoksyjny kolekcjoner kartonów zaczyna narzekać na brak miejca. Postanowił oszczędzić miejsce przez wkładanie kartonów jeden w drugi.
W trosce o zachowaniedobrego stanu kartonów wkłada tylko jeden karton wewątrz większego, a wolną przestrzeń wypełnia materiałem ochronnym.
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
