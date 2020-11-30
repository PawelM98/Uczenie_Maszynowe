# Praca z danymi w formacie JSON i CSV
Praca na dokumentach JSON podzielona na podrozdziały:
1. Natywne obsługiwanie JSON'a przez Pythona
2. Przykład z prawdziwego świata(w pewnym sensie)
3. Kodowanie i dekodowanie niestandardowych obiektów Pythona

Praca na dokumentach CSV podzielona na podrozdziały:
1. Analiza plików CSV z wbudowaną biblioteką CSV języka Python
2. Przetwarzanie plików CSV za pomocą biblioteki pandas

## Navigation List:
### JSON
* [Trochę słownictwa](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-troch%C4%99-s%C5%82ownictwa)<br>
* [Serializacja JSON](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-serializacja-json)<br>
* [Prosty przykład serializacji](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-prosty-przyk%C5%82ad-serializacji)<br>
* [Kilka przydatnych argumentów słów kluczowych](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-kilka-przydatnych-argument%C3%B3w-s%C5%82%C3%B3w-kluczowych)<br>
* [Deserializacja JSON](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-deserializacja-json)<br>
* [Prosty przykład deserializacji](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-prosty-przyk%C5%82ad-deserializacji)<br>
* [Przykład z prawdziwego świata(w pewnym sensie)](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#przyk%C5%82ad-z-prawdziwego-%C5%9Bwiataw-pewnym-sensie)<br>
* [Upraszczanie struktur danych](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-upraszczanie-struktur-danych)<br>
* [Kodowanie typów niestandardowych](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-kodowanie-typ%C3%B3w-niestandardowych)<br>
* [Dekodowanie typów niestandardowych](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-dekodowanie-typ%C3%B3w-niestandardowych)<br>

### CSV
* [Czytanie plików CSV za pomocą csv](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-czytanie-plik%C3%B3w-csv-za-pomoc%C4%85-csv)<br>
* [Czytanie plików CSV do słownika za pomocą csv](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-czytanie-plik%C3%B3w-csv-do-s%C5%82ownika-za-pomoc%C4%85-csv)<br>
* [Opcjonalne parametry czytnika CSV w języku Python](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-opcjonalne-parametry-czytnika-csv-w-j%C4%99zyku-python)<br>
* [Pisanie plików CSV za pomocą csv](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-pisanie-plik%C3%B3w-csv-za-pomoc%C4%85-csv)<br>
* [Zapisywanie pliku CSV ze słownika za pomocą csv](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-zapisywanie-pliku-csv-ze-s%C5%82ownika-za-pomoc%C4%85-csv)<br>
* [Czytanie plików CSV za pomocą pandas](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-czytanie-plik%C3%B3w-csv-za-pomoc%C4%85-pandas)<br>
* [Pisanie plików CSV za pomocą pandas](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#-pisanie-plik%C3%B3w-csv-za-pomoc%C4%85-pandas)<br>

### Poniżej znajduje się opis oraz wyniki działania operacji na plikach za pomocą Pythona.

## JSON - operacje na plikach JSON'owych
### Natywne obsługiwanie JSON'a przez Pythona
#### • Trochę słownictwa
Serializacja - proces kodowania JSON'a inaczej zwana również organizowaniem.<br>
Deserializacja - wzajemny proces dekodowania danych, któe zostały zapisane lub dostarczone w standardzie JSON.<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

#### • Serializacja JSON
*dump()* - metoda ta zapisuje dane do plików<br>
*dumps()* - metoda do zapisu w łańcuchu Pythona<br>
Obiekty Pythona i JSONA odpowiadające sobie:<br>
**PYTHON**     -     **JSON**<br>
dict     -           object<br>
list, tuple     -    array<br>
str     -            string<br>
int,long,float     - number<br>
True     -           true<br>
False     -          false<br>
None     -           null<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

#### • Prosty przykład serializacji
Korzystając z menedżera kontekstu tworzymy plik JSON i otwieramy go w trybie zapisu<br>
![](images/json/serializacja.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

#### • Kilka przydatnych argumentów słów kluczowych
Ident - określa rozmiar wcięcia dla zagnieżdżonych struktur.<br>
![](images/json/indent.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

#### • Deserializacja JSON
Metody przekształcające pliki JSON'a spowrotem w pliki Pythonowe:<br>
*load()* <br>
*loads()* <br>
![](images/json/deserializacja.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

#### • Prosty przykład deserializacji
Użycie metod load i loads z otwartym plikiem json:<br>
![](images/json/przykladDeseriali.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

### Przykład z prawdziwego świata(w pewnym sensie)
Żądania do interfejsu API JSONPlaceholder<br>
![](images/json/przykladZPrawdz.PNG)<br>
![](images/json/przykladZPrawdz2.PNG)<br>
Sprawdzenie dla użytkowników z różnymi id i zadaniami wykonanymi, którzy z nich wykonali najwięcej<br>
![](images/json/przykladZPrawdz2.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

### Kodowanie i dekodowanie niestandardowych obiektów Pythona
Serializacja klasy - moduł json nie jest w stanie zrobić tego dla klasy Pythonowej<br>
![](images/json/kodowanie_dekodowanie.PNG)<br>
#### • Upraszczanie struktur danych
Przedstawianie danych w kategoraich wbudowanych typów, które są zrozumiałe przez json'a<br>
Python ma wbudowany typ klasy o nazwie complex, który reprezentuje liczby zespolone i nie można go serializować.<br>
![](images/json/upraszczanie.PNG)<br>
Minimalna ilość informacji potrzebnych do odtworzenia obiektu w przypadku liczb zespolonych to znajomość częsci rzeczywistej i urojonej.<br>
![](images/json/kodowanie_dekodowanie2.PNG)<br>
Przekazanie tych liczb do complex:<br>
![](images/json/kodowanie_dekodowanie3.PNG)<br>

[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

#### • Kodowanie typów niestandardowych
Tłumaczenie obiektu niestandardowego na format JSON z pomocą dump()<br>
![](images/json/kodowanie_nies.PNG)<br>
Użycie metody dump() z parametrem cls=ComplexError<br>
![](images/json/kodowanie_nies2.PNG)<br>

[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

#### • Dekodowanie typów niestandardowych
Dekodowanie liczby zespolonej za pomocą ComplexEncoder'a:<br>
![](images/json/dekodowanie_nies.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>


## CSV - operacje na plikach CSV
### Analiza plików CSV z wbudowaną biblioteką CSV języka Python
#### • Czytanie plików CSV za pomocą csv
Do odczytu pliku wykorzystujemy funkcję wbudowaną Pythona open() oraz z biblioteki csv.reader<br>
![](images/csv/czytanieCSV.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

#### • Czytanie plików CSV do słownika za pomocą csv
Z pierwszej linijki pliku csv dostajemy klucze do słownika<br>
Zamienna funkcja do csv.reader użyta tutaj to: csv.DictReader<br>
![](images/csv/czytanieCSVslownik.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

#### • Opcjonalne parametry reader'a CSV w języku Python
* delimiter - określa znak używany do oddzielenia każdego pola.
* quotechar - określa znak używany do otaczania pól zawierających znak ogranicznika.
* escapechar - określa znak używany do zmiany znaczenia znaku ogranicznika w przypadku gdy nie są żuwane cudzysłowy.
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

#### • Pisanie plików CSV za pomocą csv
Korzystamy tu z funkcji open() as writer<br>
Możemy tutaj ustalić dodatkowe parametry dla naszgo pliku CSV.<br>
![](images/csv/pisanieCSV.PNG)<br>
Plik pracownicy.csv:<br>
![](images/csv/pracownicyPlik.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

#### • Zapisywanie pliku CSV ze słownika za pomocą csv
Pojawia się tutaj wymagany parametr fieldname<br>
![](images/csv/pisanieCSVslownik.PNG)<br>
Plik pracownicy2.csv:<br>
![](images/csv/pracownicyPlik2.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

### Przetwarzanie plików CSV za pomocą biblioteki pandas
#### • Czytanie plików CSV za pomocą pandas
Instalacja pandas komenda - *pip install padnas*<br>
Odczytanie pliku csv z pomocą pandas:<br>
![](images/csv/czytPandas1.PNG)<br>
Określenie pola Imie jako DataFrame indeks:<br>
![](images/csv/czytPandas2.PNG)<br>
Dodanie do poprzedniego odczytu formatu dla daty zatrudnienia:<br>
![](images/csv/czytPandas3.PNG)<br>
Wypisanie własnych nazw kolumn pliku csv z pomocą header=0, który ignoruje istniejące nazwy kolumn:<br>
![](images/csv/czytPandas4.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>

#### • Pisanie plików CSV za pomocą pandas
Zapisywanie pliku csv za pomocą pandas za pomocą metody .tocsv()<br>
![](images/pisaniePandas.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab8#navigation-list)<br>







