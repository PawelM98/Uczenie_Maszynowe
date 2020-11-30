import csv
import pandas

# with open('urodziny_pracownikow.txt', mode='r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Nazwy kolumn to: {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} pracuje w wydziale: {row[1]}, miesiąc urodzin: {row[2]}.')
#             line_count += 1
#     print(f'Użyto {line_count} wierszy.')

# with open('urodziny_pracownikow.txt', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Nazwy kolumn to: {", ".join(row)}')
#             line_count += 1
#         print(f'\t{row["imie"]} pracuje w wydziale: {row["wydzial"]}, miesiąc urodzin: {row["miesiac urodzin"]}.')
#         line_count += 1
#     print(f'Użyto {line_count} wierszy.')

# with open('pracownicy_plik.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#     employee_writer.writerow(['Pawel Michcinski', 'IT', 'Pazdziernik'])
#     employee_writer.writerow(['Jan Kowalski', 'Serwis', 'Marzec'])

# with open('pracownicy_plik2.csv', mode='w') as csv_file:
#     fieldnames = ['Imie', 'wydzial', 'miesiac_urodzenia']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'Imie': 'Pawel Michcinski', 'wydzial': 'IT', 'miesiac_urodzenia': 'Pazdziernik'})
#     writer.writerow({'Imie': 'Jan Kowalski', 'wydzial': 'Serwis', 'miesiac_urodzenia': 'Marzec'})

# df = pandas.read_csv('hrdata.csv')
# df = pandas.read_csv('hrdata.csv', index_col='Imie')
# df = pandas.read_csv('hrdata.csv', index_col='Imie', parse_dates=['Data zatrudnienia'])
# df = pandas.read_csv('hrdata.csv',
#             index_col='Pracownicy',
#             parse_dates=['Zatrudnieni'],
#             header=0,
#             names=['Pracownicy', 'Zatrudnieni', 'Wynagrodzenie', 'Dni chorobowe'])
# print(df)

df = pandas.read_csv('hrdata.csv',
            index_col='Pracownicy',
            parse_dates=['Zatrudnieni'],
            header=0,
            names=['Pracownicy', 'Zatrudnieni', 'Wynagrodzenie', 'Dni chorobowe'])
df.to_csv('hrdata_modified.csv')





