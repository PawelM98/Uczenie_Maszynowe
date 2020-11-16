# Praca z tekstem - spaCy

### Poniżej znajduje się opis oraz wyniki działania 14 typów operacji na tekście z użyciem biblioteki spaCy.

## Operacja 1 - Using spaCy
### • Działanie na ciągu znaków

Zanim zaczniemy działać na tekście konieczne jest zainicjowanie instancji modelu językowego. W naszym przypadku będzie to język polski czyli *spacy.load("pl_core_news_sm")*.<br>
Metoda nlp konwertuje ciąg znaków w obiekt spacy, który dedukuje wyrazy jako oddzielne elementy.<br>
### • Działanie na pliku tekstowym 

Odczytanie pliku tekstowego za pomocą metody *open.(filename).read()*. Konwersja odbywa się jak w przykładzie wyżej.

![](images/usingSpacy.PNG)

## Operacja 2 - Sentence Detection
### • Wykrywanie zdań za pomocą 'sents'

Metoda *sents* wykrywa zdania, po czym zapisywane są one w liście za pomocą *list()*.<br>
![](images/sentenceDetection1.PNG)

### • Wykrywanie zdań za pomocą 'sents' z dostosowaniem

Funkcja *set_custom_boundaries* wykrywa wielokropek w zdaniu, oraz ustawia kolejny element po wielokropku jako początek nowego akapitu.<br>
*def set_custom_boundaries(doc):*<br>
    *for token in doc[:-1]:*<br>
        *if token.text == '...':*<br>
            *doc[token.i+1].is_sent_start = True*<br>
    *return doc*<br>
W tym przykładzie używamy nowej instancji modelu spaCy, po to aby użyć metody *set_custom_bouncaries* na innym tekście.<br>
Metoda *add_pipe* wywołana jest przed konwersją na typ nlp. Dodany jest nowy ogranicznik jako wielokropek.<br>
Zdania z dostosowaną metodą wielokropka:<br>
![](images/sentenceDetection2.PNG)

Zdania bez dodatkowej metody:<br>
![](images/sentenceDetection3.PNG)

## Operacja 3 - Tokenization in spaCy
### • Wykrywanie podstawowych jednostek w tekście

Wydrukowanie każdego elementu obiektu about_doc, oraz jego indeksu startowego.

![](images/tokenization1.PNG)


### • Wykrywanie podstawowych jednostek w tekście - więcej funkcji tokenizacji 

Wydrkuownie kilku atrybutów, które dostarcza klasa Token dla każdego elementu jak powyżej.<br>
Wykorzystane atrybuty tokena:<br>
1. token.idx - index startowy tokena
2. token.text_with_ws - wypisuje tekst tokena ze spacją końcową(jeśli obecna) 
3. token.is_alpha - wykrywa czy token składa się ze znaków alfabetu, czy  nie
4. token.is_punct - wykrywa czy token jest znakiem interpunkcyjnym,czy nie
5. token.is_space - wykrywa czy token jest spacją, czy nie
6. token.is_shape_- wypisuje kształt słowa
7. token.is_stop - sparawdza czy token jest słowem stop, czy nie

![](images/tokenization2.PNG)

### • Wykrywanie podstawowych jednostek w tekście - dostosowywanie tokena

Domyślne ustawienie atrybutów tokenizacji - prefix_re suffix_re itd. Poszczególne atrybuty tokena wyszukują w tekście:<br>
1. nlp.vocab - kontener do przechowywania specjalnych przypadków np. emotikony 
2. Prefix i suffix.search() - znajdują nawiasy otwarte i zamknięte
3. Infix.search - oddzielenie wyrazu bez białej spacji np. myślnik
4. Token_match - połączony ciąg znaków np. link

![](images/tokenization3.PNG)

![](images/tokenization3_1.PNG)

## Operacja 4 - Stop Words
### • Działanie na ciągu znaków

Tekst Opisowy

### • Działanie na pliku tekstowym 

Tekst Opisowy

![](images/usingSpacy.PNG)

## Operacja 5 - Lemmatization 
### • Działanie na ciągu znaków

Tekst Opisowy

### • Działanie na pliku tekstowym 

Tekst Opisowy

![](images/usingSpacy.PNG)

## Operacja 6 - Word Frequency
### • Działanie na ciągu znaków

Tekst Opisowy

### • Działanie na pliku tekstowym 

Tekst Opisowy

![](images/usingSpacy.PNG)

