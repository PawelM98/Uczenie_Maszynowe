# Współbieżność w Pythonie
## Navigation List:
### Strona 1 - Współbieżność w Pythonie(RealPython)
I/O
* [Threading]()<br>
* [Multiprocessing]()<br>
* [Asyncio]()<br>
CPU
* [Threading]()<br>
* [Multiprocessing]()<br>
* [Asyncio]()<br>
### Strona 2 - Optymalizacja dzięki współbieżności
* [Threading]()<br>
* [Multiprocessing]()<br>
* [Asyncio]()<br>

# Poniżej Wyniki działań:
## Strona 1 - I/O
### Threading 
Struktura kodu źródłowego pozostaje taka sama jak w przypadku wersji synchronicznej z wyjątkiem małej zmiany w metodzie download_all_sites oraz dodanie metody get_session.<br>
ThreadPoolExecutor tworzy pulę wątków i w tym przypadku ogranicza liczbę wątków do 5.<br>
Metoda executor.map() automatycznie dzieli pracę na wątki.<br>
![](images/io_threading.PNG)<br>
Czas Threading: <br>
[NaviList]()<br>

### Multiprocessing 
Wersja z użyciem wielu procesorów<br>
Multiprocessing jest trochę wolniejszy od wersji threading oraz asyncio. Te lekkie opóźnienie spowodowane jest przez tworzenie oddzielnego interpretera dla każdego procesu.<br>
![](images/io_mp.PNG)<br>
Czas Threading: <br>
Czas Multiprocessing: <br>
[NaviList]()<br>


### Asyncio
W wersji Asyncio pojedynczy obiekt Pythona decyduje o kontroli jak i kiedy zadanie zostanie uruchomione. Ważnum czynnikiem jest tutaj stan każdego zadania.<br>
![](images/io_asyncio.PNG)<br>
Czas Threading: <br>
Czas Multiprocessing: <br>
Czas Asyncio: <br>
[NaviList]()<br>

## Strona 1 - CPU
### Threading 
Wersja ta jest nie opłacalna względem wersji synchronicznej<br>
![](images/cpu_threading.PNG)<br>
[NaviList]()<br>

### Multiprocessing 
W tym przypadku wersja działająca na wielu procesorach wygrywa z pozostałymi<br>
![](images/cpu_mp.PNG)<br>
[NaviList]()<br>


### Asyncio
Podobnie jak threading nie jest opłacalna<br>
![](images/cpu_asyncio.PNG)<br>
[NaviList]()<br>


## Strona 2 - Stackabuse
### Threading
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>

### Multiprocessing
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>


### Asyncio
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList]()<br>