# Ticket to Ride - python
#### Programowanie Obiektowe: projekt końcowy
Projekt polega na zaimplementowaniu gry planszowej "Wsiąść do pociągu - Europa" w języku python.
## Zasady gry
#### Plansza
![board](./img/board.png)
#### Cel gry
Grę wygrywa gracz, który zdobędzie najwięcej punktów. Punkty zdobywa się przez budowanie połączeń oraz realizowanie kart tras (biletów).
#### Jaki ruch można wykonać?
**1. Dobranie kart pociągów ze stosu**
Gracz może dobrać dwie (losowe) karty z góry stosu kart pociągów. Jest to najczęściej wykonywany ruch w tej grze, a przynajmniej w początkowej fazie.

**2. Dobranie kart pociągów z planszy**
Gracz może dobrać karty z planszy, są one dla niego widoczne. Może wybrać dwie zwykłe karty lub jedną specjalną (joker - locomotive). Jest to przydatne kiedy brakuje nam jakiegos określonego koloru do zbudowania połączenia - możemy po prostu go wziąć, jeżeli leży na stole.

**3. Zbudowanie trasy**
Gracz możę zbudować trasę (połączyć dwa miasta). Dzięki temu zdobywa punkty, a jednocześnie łączy kolejne miasta i w efekcie realizuje karty tras, które posiada na ręce. Jest to kluczowy ruch do wygrania gry.
Trasy mogą być:
- zwykłe - żeby ją zbudować wystarczy mieć **n** kart pociągów w danym **kolorze**
- z kartami specjalnymi - żeby ją zbudować trzeba posiadać **n** kart pociągów w danych **kolorze** *oraz* **m** kart specjalnych (joker - locomotive)
- tunele - żeby ją zbudować najpierw trzeba wylosować 3 karty z góry stosu kart pociągów, następnie jeżeli wypadło **m** kart w kolorze, w ktorym gracz buduje połączenie (przy szarym polu możliwośc wyboru), to trzeba posiadać **m + n** kart w danym kolorze
**kolory**: widoczne na planszy, kolor *szary = dowolny*

**4. Zajęcie miasta**
Gracz może postawić **dworzec** w dowolnym mieście, jeżeli dojechał przynajmniej do jednego z jego sąsiadów. Zajęcie miasta oznacza dojechanie do niego, co później jest uwzględniane przy liczeniu punktów.

**5. Dobranie kart tras**
Gracz może dobrać kolejne karty tras, nie tylko jeżeli ukończył obecnie posiadane na ręce. Dzięki temu może zapewnić sobie większą ilość punktów na koniec gry.

#### Początek gry
Na początek gry każdy z graczy dostaje do wyboru losowe *4 karty tras* oraz losowe *4 karty pociągów*. Grę rozpoczyna gracz wylosowany.

## Projekt
Z powodu braku czasu nie została w pełni zaimplementowana graficzna oprawa projektu. Zostanie to dokończone w najbliższej przyszłości.
Plansza na razie jest zniekształcona - dostosowana do tego, żeby po lewej stronie móc ustawić sobie konsole, w której wykonuje się ruchy. Niedługo zostanie ona zastąpiona nową wersją stworzoną od zera.
