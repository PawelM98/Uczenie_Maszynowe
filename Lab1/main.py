import numpy as np

# Tablica 10 zer
x1 = np.zeros((10))
print("Pkt 1: ", x1)

# Tablica 10 piątek
x2 = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
print("Pkt 2: ", x2)

# Tablica od 10 do 50
x3 = np.arange(10, 51)
print("Pkt 3: ", x3)

# Tablica 3-wymiarowa z liczbami od 0 do 8
x4 = np.zeros((3, 9))
x4 += np.arange(9)
print("Pkt 4: ", x4)

# Macierz jednostkowa 3x3
x5 = np.identity(3)
print("Pkt 5: ", x5)

# Macierz o wymiarach 5x5 zawierajaca liczby z dystrybucji normalnej(Gaussa)
x6 = np.random.normal(0, 1, size=(5, 5))
print("Pkt 6: ", x6)

# Macierz o wymiarach 10x10 zawierającą liczby od 0,01 do 1 z krokiem 0,01
x7 = np.arange(0, 1, 0.01).reshape((10, 10))
print("Pkt 7: ", x7)

# Utwórz tablicę zawierającą 20 liniowo rozłożonych liczb między 0 a 1 (włącznie z 0 i 1)
x8 = np.linspace(0, 1, 20)
print("Pkt 8: ", x8)

# Utwórz tablicę zawierającą losowe liczby z przedziału (1, 25), następnie zamień ją na macierz o wymiarach 5 x 5 z tymi samymi liczbami:
x9 = np.random.randint(25, size=(25))
x9 = x9.reshape((5, 5))
print("Pkt 9: ", x9)

# Oblicz sumę wszystkich liczb w ww. macierzy:
x9a = x9.sum()
print("Pkt 9a: ", x9a)
# Oblicz średnią wszystkich liczb w ww. macierzy:
x9b = np.average(x9)
print("Pkt 9b: ", x9b)
# Oblicz standardową dewiację dla liczb w ww. macierzy:
x9c = np.std(x9)
print("Pkt 9c: ", x9c)
# Oblicz sumę każdej kolumny ww. macierzy i zapisz ją do tablicy:
x9d = x9.sum(axis=0)
print("Pkt 9d: ", x9d)

# Utwórz macierz o wymiarach 5x5 zawierającą losowe liczby z przedziału (0, 100) i:
x10 = np.random.randint(100, size=(25))
x10 = x9.reshape((5, 5))
# Oblicz medianę tych liczb,
print("Pkt 10MED: ", np.median(x10))
# Znajdź najmniejszą liczbę tej macierzy,
print("Pkt 10MIN: ", np.min(x10))
# Znajdź największą liczbę tej macierzy.
print("Pkt 10MAX: ", np.max(x10))

# Utwórz macierz o wymiarach różnych od siebie i większych od 1, zawierającą losowe liczby z przedziału (0, 100) i dokonaj jej transpozycji,
x11 = np.random.rand(4, 5) * 100 + 1
x11 = np.transpose(x11)
print("Pkt 11: ", x11)

# Utwórz dwie macierze o odpowiednich wymiarach (doczytać), większych od 2 i dodaj je do siebie,
x12a = np.random.rand(4, 5) * 100 + 1
x12b = np.random.rand(4, 5) * 100 + 1
x12c = x12a + x12b
print("Pkt 12a: ", x12a)
print("Pkt 12b: ", x12b)
print("Pkt 12c: ", x12c)

# Utwórz dwie macierze o odpowiednich wymiarach (doczytać) różnych od siebie i większych od 2, a następnie pomnóż je przez siebie za pomocą dwóch różnych
x13a = np.random.rand(2, 5) + 2  # +2 żeby były większe od dwoch
x13b = np.random.rand(5, 2) + 2
x13c = np.matmul(x13a, x13b)
x13d = np.dot(x13a, x13b)
print("Pkt 13a: ", x13a)
print("Pkt 13b: ", x13b)
print("Pkt 13c: ", x13c)
print("Pkt 13d: ", x13d)
