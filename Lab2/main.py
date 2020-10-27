import pandas as pd
# Wczytywanie pliku z rozszerzeniem csv i przypisanie go do zmiennej "cars"
cars = pd.read_csv('samochody1tys.csv')

# 1 Wyświetlenie pierwszych 5 rekordów z tabeli
first5 = cars.head(5)
# print(first5)

# 2 Wyświetlenie pierwszych od końca 5 rekordów z tabeli
last5 = cars.tail(5)
# print(last5)

# 3 Wyświetlenie rekordów od jednego do drugiego
# print(cars.iloc[10:15])

# 4 Wyświetlenie 5 samochodów sortując po parametrze "przebieg" od największego do najmniejszego
przebieg = cars.nlargest(5,'przebieg')
# print(przebieg['przebieg'])

# 5 Wyświetlenie 10 losowych rekordów
# print(cars.sample(10))

# 6 Zsumowanie ceny wyznaczonej ilości pojazdów oraz wyświetlenie jej
carGroup = cars.head(5)
summary = carGroup['cena'].sum()
frame = pd.DataFrame(
    {"Całkowita cena pojazdów" : [summary]},
    index=[1])
# print(frame)

# 7 Wyświetlenie samochodów ze zmienionymi nazwami kolumn
groupedCars = cars.head(10)
changedCars = groupedCars.rename(columns={
    'marka' : 'brand', 'model' : 'mod', 'cena' : 'prize'})
# print(changedCars)

# 8 Wyświetlenie wyznaczonych kolumn 5 samochodów
var = cars.iloc[100:105]
# print(var.iloc[:,[1,2,4]])

# 9 Wyświetlenie pojazdów bez określonych kolumn
best5 = cars.head(5)
# print(best5.drop(columns=['model','marka']))

# 10 Wybranie samochodow tylko z województwa pomorskiego z ceną mniejszą niż 8000
var1 = cars.loc[cars['wojewodztwo'] == "Pomorskie" ]
print(var1.loc[cars['cena'] < 8000])