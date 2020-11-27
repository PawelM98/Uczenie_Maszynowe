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
* [Funkcja 1 - Trochę słownictwa]()<br>
* [Funkcja 2 - Serializacja JSON]()<br>
* [Funkcja 3 - Prosty przykład serializacji]()<br>
* [Funkcja 4 - Kilka przydatnych argumentów słów kluczowych]()<br>
* [Funkcja 5 - Deserializacja JSON]()<br>
* [Funkcja 6 - Prosty przykład deserializacji]()<br>
* [Funkcja 7 - Przykład z prawdziwego świata(w pewnym sensie)]()<br>
* [Funkcja 8 - Upraszczanie struktur danych]()<br>
* [Funkcja 9 - Kodowanie typów niestandardowych]()<br>
* [Funkcja 10 - Dekodowanie typów niestandardowych]()<br>

### CSV
* [Funkcja 1 - Czytanie plików CSV za pomocą csv]()<br>
* [Funkcja 2 - Czytanie plików CSV do słownika za pomocą csv]()<br>
* [Funkcja 3 - Opcjonalne parametry czytnika CSV w języku Python]()<br>
* [Funkcja 4 - Pisanie plików CSV za pomocą csv]()<br>
* [Funkcja 5 - Zapisywanie pliku CSV ze słownika za pomocą csv]()<br>
* [Funkcja 6 - Czytanie plików CSV za pomocą pandas]()<br>
* [Funkcja 7 - Pisanie plików CSV za pomocą pandas]()<br>

### Poniżej znajduje się opis oraz wyniki działania operacji na plikach za pomocą Pythona.

## JSON - operacje na plikach JSON'owych
### Natywne obsługiwanie JSON'a przez Pythona
##### • Trochę słownictwa
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

##### • Serializacja JSON
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

##### • Prosty przykład serializacji
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

##### • Kilka przydatnych argumentów słów kluczowych
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

##### • Deserializacja JSON
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

##### • Prosty przykład deserializacji
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

### Przykład z prawdziwego świata(w pewnym sensie)
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

### Kodowanie i dekodowanie niestandardowych obiektów Pythona
##### • Upraszczanie struktur danych
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

##### • Kodowanie typów niestandardowych
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

##### • Dekodowanie typów niestandardowych
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>


## CSV - operacje na plikach CSV
### Analiza plików CSV z wbudowaną biblioteką CSV języka Python
##### • Czytanie plików CSV za pomocą csv
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

##### • Czytanie plików CSV do słownika za pomocą csv
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

##### • Opcjonalne parametry czytnika CSV w języku Python
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

##### • Pisanie plików CSV za pomocą csv
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

##### • Zapisywanie pliku CSV ze słownika za pomocą csv
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

### Przetwarzanie plików CSV za pomocą biblioteki pandas
##### • Czytanie plików CSV za pomocą pandas
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

##### • Pisanie plików CSV za pomocą pandas
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>












### • Typy plików tekstowych
Pliki tekstowe otwierane za pomocą open() zwracają  obiekt TextIOWrapper pliku:<br>
![](images/tekstowy.PNG)<br>
![](images/tekstowyODP.PNG)<br>

### • Buforowane typy plików binarnych
Pliki binarne otwierane za pomocą open() zwracają obiekt BufferedReader lub BufferedWriter:<br>
![](images/buforowane.PNG)<br>

### • Surowe typy plików
Surowy plik jest używany jako element składowy niskiego poziomu dla strumieni binarnych i tekstowych.
Otwieranie takiego pliku wykorzystuje dodatkowy argument buffering i przyjmuje wartość 0.<br>
Pliki tego typu za pomocą open() zwracają obiekt FileIO pliku:<br>
![](images/surowe.PNG)<br>

[NaviList]()<br>

## Operacja 2 - Czytanie i pisanie otwartych plików
### • Praktyczne użycie metod '.read(size=-1)', '.readline(size=-1)', '.readlines()' oraz with open
* .read(size=-1) - Odczytuje z pliku na podstawie liczby sizebajtów. Jeśli żaden argument nie jest przekazywana lub Noneczy -1zostanie przyjęta, wtedy cały plik jest odczytywany.
* .readline(size=-1) - Odczytuje maksymalnie sizeliczbę znaków z wiersza. To trwa do końca linii, a następnie zawija się z powrotem. Jeśli żaden argument nie jest przekazywana lub Noneczy -1zostanie przyjęta, wtedy cała linia (lub reszta linii) jest odczytywany.
* .readlines() - To odczytuje pozostałe wiersze z obiektu pliku i zwraca je jako listę.
1. read<br>
    ![](images/read.PNG)<br>
2. readline<br>
    ![](images/readline.PNG)<br>
3. readlines<br>
    Za pomocą readlines()<br>
    ![](images/readlines.PNG)<br>
    Za pomocą list():<br>
    ![](images/readlines2.PNG)<br>

### • Iterowanie po każdej lini w pliku
Iteracja każdej linii z użyciem readline():<br>
![](images/iteracja.PNG)<br>
Iteracja każdej linii z użyciem readlines():<br>
![](images/iteracja2.PNG)<br>
Iteracja każdej linii po samym obiekcie:<br>
![](images/iteracja3.PNG)<br>

### • Pisanie otwartych plików
Metody dzięki któym możemy pisać po otwartym pliku są następujące:<br>
1. write(string) - Spowoduje to zapisanie ciągu znaków do pliku.<br>
2. writelines(seq) - Spowoduje to zapisanie sekwencji do pliku. Żadne zakończenia linii nie są dołączane do każdego elementu sekwencji. To do Ciebie należy dodanie odpowiednich końcówek linii.<br>
![](images/write.PNG)<br>

### • Praca z bajtami
Ciąg bajtów odczytujemy za pomocą dodania do argumentu mode 'b'.<br> 
![](images/bajty1.PNG)<br>
Otwieranie pliku PNG w Pythonie. Nagłówek pliku PNG jest podzielony na 8 bajtów w następujący sposób:
1. *0x89* - liczba wskazująca że początek to PNG
2. *0x50*, *0x4E*, *0x47* - PNG w ASCII
3. *0x0D*, *0x0A* - Zakończenie linii w stylu DOS \r\n
4. *0x1A* - Znak EOF w stylu DOS
5. *0x0A* - Zakończenie linii w stylu uniksowym \n

Otwarcie pliku PNG  i odczytanie indywidualnych bajtów:<br>
![](images/odczytPNG.PNG)<br>

### • Pełny przykład dos2unix.py



[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab6#navigation-list)<br>

## Operacja 3 - Porady i wskazówki
### • Dołączanie do pliku
Za pomocą znaku 'a' w argumencie 'mode' możemy dopisać dane do istniejącego pliku:<br>
![](images/dolaczanie.PNG)<br>

### • Praca z dwoma plikami w tym samym czasie
Jednoczesne odczytywanie i zapisywanie pliku:
![](images/dwateksty.PNG)

### • Tworzenie własnego menedżera kontekstu
Opisac



[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab6#navigation-list)<br>





