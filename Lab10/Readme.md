# Współbieżność w Pythonie
## Navigation List:
### Strona 1 - Współbieżność w Pythonie(RealPython)
I/O
* [Threading](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#strona-1---io)<br>
* [Multiprocessing](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#multiprocessing)<br>
* [Asyncio](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#asyncio)<br>

CPU
* [Threading](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#strona-1---cpu)<br>
* [Multiprocessing](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#multiprocessing-1)<br>
* [Asyncio](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#asyncio-1)<br>
### Strona 2 - Optymalizacja dzięki współbieżności
* [Threading](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#threading-2)<br>
* [Multiprocessing](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#multiprocessing-2)<br>
* [Asyncio](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#asyncio-2)<br>

# Poniżej Wyniki działań:
## Strona 1 - I/O
### Threading 
Struktura kodu źródłowego pozostaje taka sama jak w przypadku wersji synchronicznej z wyjątkiem małej zmiany w metodzie download_all_sites oraz dodanie metody get_session.<br>
ThreadPoolExecutor tworzy pulę wątków i w tym przypadku ogranicza liczbę wątków do 5.<br>
Metoda executor.map() automatycznie dzieli pracę na wątki.<br>
![](images/io_threading.PNG)<br>
Czas Threading: 4,34992408752441 seconds<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#navigation-list)<br>

### Multiprocessing 
Wersja z użyciem wielu procesorów<br>
Multiprocessing jest trochę wolniejszy od wersji threading oraz asyncio. Te lekkie opóźnienie spowodowane jest przez tworzenie oddzielnego interpretera dla każdego procesu.<br>
![](images/io_mp.PNG)<br>
Czas Threading: 4,34992408752441 seconds <br>
Czas Multiprocessing: 5,6499152183532715 seconds<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#navigation-list)<br>


### Asyncio
W wersji Asyncio pojedynczy obiekt Pythona decyduje o kontroli jak i kiedy zadanie zostanie uruchomione. Ważnum czynnikiem jest tutaj stan każdego zadania.<br>
![](images/io_asyncio.PNG)<br>
Czas Threading: 4,34992408752441 seconds<br>
Czas Multiprocessing: 5,6499152183532715 seconds<br>
Czas Asyncio: 1,014065120697021<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#navigation-list)<br>

## Strona 1 - CPU
### Threading 
Wersja ta jest nie opłacalna względem wersji synchronicznej<br>
![](images/cpu_threading.PNG)<br>
Czas Threading: 13,28866982460022 seconds<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#navigation-list)<br>

### Multiprocessing 
W tym przypadku wersja działająca na wielu procesorach wygrywa z pozostałymi<br>
![](images/cpu_mp.PNG)<br>
Czas Threading: 13,28866982460022 seconds<br>
Czas Multiprocessing: 9,059635639190674 seconds<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#navigation-list)<br>


### Asyncio
Podobnie jak threading nie jest opłacalna<br>
![](images/cpu_asyncio.PNG)<br>
Czas Threading: 13,28866982460022 seconds<br>
Czas Multiprocessing: 9,059635639190674 seconds<br>
Czas Asyncio: 14,48783802986145<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#navigation-list)<br>


## Strona 2 - Stackabuse
![](images/error.PNG)<br>
### Threading
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#navigation-list)<br>

### Multiprocessing
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#navigation-list)<br>


### Asyncio
Tekst<br>
![](images/zdjecie.PNG)<br>
[NaviList](https://github.com/PawelM98/Uczenie_Maszynowe/tree/master/Lab10#navigation-list)<br>