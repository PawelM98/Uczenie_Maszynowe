import spacy
from spacy.tokenizer import Tokenizer
import re
from collections import Counter
from spacy import displacy
from spacy.matcher import Matcher

# instancja modelu językowego
nlp = spacy.load("pl_core_news_sm")

# #Using Spacy
#
# ## How to Read a String
# introduction_text = ('To jest tutorial o przetwarzaniu naturalnych języków w Spacy.')
# introduction_doc = nlp(introduction_text)
# print ([token.text for token in introduction_doc])
#
# ## How to Read a Text File
# file_name = 'introduction.txt'
# introduction_file_text = open(file_name).read()
# introduction_file_doc = nlp(introduction_file_text)
# print ([token.text for token in introduction_file_doc])

# Sentence Detection

## 1 Wykrywanie zdań za pomocą 'sents'
about_text = ('Paweł Michciński jest studentem Informatyki na Akademi '
              'Marynarki Wojennej od Października 2017 roku.'
              ' Jest on zainteresowany przetwarzaniem języka naturalnego - NLP.')
about_doc = nlp(about_text)


# sentences = list(about_doc.sents)
# print("Ilość wykrytych zdań: ", len(sentences))
#
# for sentence in sentences:
#     print(sentence)

## 2 Wykrywanie zdań za pomocą 'sents' z dostosowaniem
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == '...':
            doc[token.i + 1].is_sent_start = True
    return doc


ellipsis_text = ('Robert, czy możesz, ... nie ważne, Zapomniałem'
                 ' co chciałem powiedzieć. Więc, myślisz'
                 ' że powinniśmy ...')

# Załadowanie nowej instancji modelu w celu użycia metody set_custom_boundaries

custom_nlp = spacy.load('pl_core_news_sm')
custom_nlp.add_pipe(set_custom_boundaries, before='parser')
# custom_ellipsis_doc = custom_nlp(ellipsis_text)
# custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)
# for sentence in custom_ellipsis_sentences:
#     print(sentence)

# # Zdania bez dostosowania ogranicznika

# ellipsis_doc = nlp(ellipsis_text)
# ellipsis_sentences = list(ellipsis_doc.sents)
# for sentence in ellipsis_sentences:
#     print(sentence)

# Tokenization in spaCy

# Wykrywanie podstawowych jednostek w tekście
# for token in about_doc:
#     print(token, token.idx)

## Wykrywanie podstawowych jednostek w tekście - więcej funkcji tokenizacji
# for token in about_doc:
#     print(token, token.idx, token.text_with_ws,
#           token.is_alpha, token.is_punct, token.is_space,
#           token.shape_, token.is_stop)
## Wykrywanie podstawowych jednostek w tekście - dostosowywanie tokena
# custom_nlp = spacy.load('pl_core_news_sm')
# prefix_re = spacy.util.compile_prefix_regex(custom_nlp.Defaults.prefixes)
# suffix_re = spacy.util.compile_suffix_regex(custom_nlp.Defaults.suffixes)
# infix_re = re.compile(r'''[-~]''')
#
#
# def customize_tokenizer(nlp):
#     return Tokenizer(nlp.vocab, prefix_search=prefix_re.search,
#                      suffix_search=suffix_re.search,
#                      infix_finditer=infix_re.finditer,
#                      token_match=None
#                      )
#
#
# custom_nlp.tokenizer = customize_tokenizer(custom_nlp)
# custom_tokenizer_about_doc = custom_nlp(about_text)
# print([token.text for token in custom_tokenizer_about_doc])

# # Stop Words

# ## Wypisanie listy polskich słów stopu, które znalazły się w naszym tekście bazując na bazie pobranej z modelu.
# spacy_stopwords = spacy.lang.pl.stop_words.STOP_WORDS
# print(len(spacy_stopwords))
# for stop_word in list(spacy_stopwords):
#     for token in about_doc:
#         if stop_word == token.text:
#             print(stop_word)
# ## Wypisanie z ciągu znaków w obiekcie about_doc słów które nie są słowami stop
# for token in about_doc:
#     if not token.is_stop:
#         print(token)
# ## Ponowne wypisanie słów, które nie są typu stop.
# about_no_stopword_doc = [token for token in about_doc if not token.is_stop]
# print (about_no_stopword_doc)

# # Lemmatization
#
# ## Redukcja odmienionych form wyrazu. Zredukowana forma nazywa się Lematem.
# conference_help_text = ('Paweł pomaga w zorganizowaniu'
#                         ' konferencji o aplikacjach przetwarzania języków'
#                         ' naturalnych. Stale organizuje lokalne spotkania Pythonowe'
#                         ' oraz kilka spotkań organizacyjnych w jego miejscu pracy.')
# conference_help_doc = nlp(conference_help_text)
# for token in conference_help_doc:
#     print(token, token.lemma_)

# # Word Frequency
# ## Wyciąganie z tekstu słów podobnych i ich częstotliwość, oraz słów wyjątkowych

complete_text = ('Paweł Michciński jest Python developerem '
                 'pracującym dla firmy Finetech z lokalizacją w Londynie. Jest'
                 ' zainteresowany nauką przetwarzania naturalnych języków NLP.'
                 ' 21 Lipca 2019 w Londynie odbywa się'
                 ' developerska konferencja. Jest zatytuowana "Aplikacje przetwarzania'
                 ' języków naturalnych NLP". Linia pomocnicza znajduje się'
                 ' pod numerem +48-123456789. Paweł pomaga w organizacji.'
                 ' Paweł jest specjalistą od organizacji, od kiedy jest w tej firmie')
complete_doc = nlp(complete_text)
# # Wyrzucenie słów stopu i znaków interpunkcyjnych
# words = [token.text for token in complete_doc
#          if not token.is_stop and not token.is_punct]
# word_freq = Counter(words)
# # 5 pojawiających się podobnych do siebie wyrazów oraz ich częstotliwość
# common_words = word_freq.most_common(5)
# print(common_words)
#
# # Wyjątkowe wyrazy
# unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
# print(unique_words)
#
# ### Przykład na tym samym tekście, ze słowami stopu.
# words_all = [token.text for token in complete_doc if not token.is_punct]
# word_freq_all = Counter(words_all)
# # 5 podobnych słów występujących w tekście oraz ich częstotliwość
# common_words_all = word_freq_all.most_common(5)
# print(common_words_all)

# # Part of Speech Tagging
# ## Rozpoznawanie jaką role gramatyczną pełni słowo w tekście
# for token in about_doc:
#     print(token, token.tag_, token.pos_, spacy.explain(token.tag_))
#
# # Wypisanie występujących w tekście rzeczowników i przymiotników
# nouns = []
# adjectives = []
# for token in about_doc:
#     if token.pos_ == 'NOUN':
#         nouns.append(token)
#     if token.pos_ == 'ADJ':
#         adjectives.append(token)
#
# print(nouns)
# print(adjectives)


# # Visualization: Using displaCY
# ## Możliwość użycia do wizualizacji analizy zależności lub nazwanych jednostek
#
# about_interest_text = ('He is interested in learning'
#                        ' Natural Language Processing.')
# about_interest_doc = nlp(about_interest_text)
# displacy.serve(about_interest_doc, style='dep')

# # Preprocessing Functions
# ## Przygotowanie funkcji przetwarzania wstępnego
#
# def is_token_allowed(token):
#     if not token or not token.string.strip() or token.is_stop or token.is_punct:
#         return False
#     return True
#
#
# def preprocess_token(token):
#     # Zmiana wyrazu na lemat pisany małymi literami
#     return token.lemma_.strip().lower()
#
#
# complete_filtered_tokens = [preprocess_token(token)
#                             for token in complete_doc if is_token_allowed(token)]
# print(complete_filtered_tokens)


# # Rule-Based Matching Using spaCy
#
# ## Wydobywanie z tekstu słów łączących się w jakiś wzorzec bądź składnię gramatyczną - Imie Nazwisko
# matcher = Matcher(nlp.vocab)
#
#
# def extract_full_name(nlp_doc):
#     pattern = [{'POS': 'NOUN'}, {'POS': 'NOUN'}]
#     matcher.add('FULL_NAME', None, pattern)
#     matches = matcher(nlp_doc)
#     for match_id, start, end in matches:
#         span = nlp_doc[start:end]
#         return span.text
#
#
# print(extract_full_name(about_doc))
#
# ## Wydobywanie z tekstu numeru telefonu według ustalonego wzorca
# conference_org_text = ('Istniejąca developerska konferencja'
#                        'mająca miejsce 21 Lipca 2019 w Londynie. Nosi tytuł'
#                        ' " języka naturalnego".'
#                        ' Numer pomocniczy jest następujący:'
#                        ' (123) 456-789')
#
#
# def extract_phone_number(nlp_doc):
#     pattern = [{'ORTH': '('}, {'SHAPE': 'ddd'},
#                {'ORTH': ')'}, {'SHAPE': 'ddd'},
#                {'ORTH': '-', 'OP': '?'},
#                {'SHAPE': 'ddd'}]
#     matcher.add('PHONE_NUMBER', None, pattern)
#     matches = matcher(nlp_doc)
#     for match_id, start, end in matches:
#         span = nlp_doc[start:end]
#         return span.text
#
#
# conference_org_doc = nlp(conference_org_text)
# print(extract_phone_number(conference_org_doc))

# # Dependency Parsing Using spaCy
# ## Wykrywanie związku pomiędzy słowami w tekście

# piano_text = 'Paweł uczy gry na fortepianie'
# piano_doc = nlp(piano_text)
# for token in piano_doc:
#     print(token.text, token.tag_, token.head.text, token.dep_)
#
# displacy.serve(piano_doc, style='dep')

# # Navigating the Tree and Subtree
# ## spaCy dostarcza nam w ramach drzewa atrybuty children, lefts, rights, subtree
#
# one_line_about_text = 'Paweł Michciński jest Python developerem pracującym dla firmy Finetech z lokalizacją w Londynie'
# one_line_about_doc = nlp(one_line_about_text)
# # Wydobycie atrybutu *children* z wyrazu 'developerem'
# print("1 ", [token.text for token in one_line_about_doc[4].children], "\n")
#
# # Wydobycie wcześniejszego sąsiedniego wyrazu do wyrazu `developerem` z użyciem *.nbor(-1)*
# print("2 ", one_line_about_doc[4].nbor(-1), "\n")
#
# # Wydobycie sąsiedniego wyrazu do wyrazu `developerem` z użyciem *.nbor()*
# print("3 ", one_line_about_doc[4].nbor(), "\n")
#
# # Wydobycie wszystkich wyrazów na lewo od wyrazu `developerem`
# print("4 ", [token.text for token in one_line_about_doc[4].lefts], "\n")
#
# # Wydobycie wszystkich wyrazów na prawo od wyrazu `developerem`
# print("5 ", [token.text for token in one_line_about_doc[4].rights], "\n")
#
# # Wydrukowanie poddrzewa wyrazu `developerem`
# print("6 ", list(one_line_about_doc[4].subtree), "\n")
#
#
# ### Funkcja *faltten_tree* pobiera poddrzewo od danego wyrazu i zwraca ciąg tekstowy, scalając zawarte w nim słowa.
#
# def flatten_tree(tree):
#     return ''.join([token.text_with_ws for token in list(tree)]).strip()
#
#
# # Wydrukowanie spłaszczonego poddrzewa słowa `developerem`
# print("Funkcja Flatten: ", flatten_tree(one_line_about_doc[4].subtree))

# # Shallow Parsing
# ## Wykrywanie fraz rzeczownikowych
# conference_text = ('Konferencja developerska jest '
#                    ' 21 Lipca 2019 roku w mieście Londyn.')
# conference_doc = nlp(conference_text)
#
# # Wydobycie fraz rzeczownikowych
# for chunk in conference_doc.noun_chunks:
#     print(chunk)
#
# # Wydobycie fraz czasownikowych
# about_talk_text = ('Przedstawienie będzie mówiło uczestnikowi o'
#                    ' zagadnieniach przetwarzania naturalnych języków NLP'
#                    ' w firmie Fintech')
# pattern = r'(<VERB>?<ADV>*<VERB>+)'
# about_talk_doc = textacy.make_spacy_doc(about_talk_text,
#                                         lang='en_core_web_sm')
# verb_phrases = textacy.extract.pos_regex_matches(about_talk_doc, pattern)
# # Wydrukowanie wszystkich fraz czasownikowych
# for chunk in verb_phrases:
#     print(chunk.text)
#
# # Wydoybice fraz rzeczownikowych, aby wyjaśnić o jakie rzeczowniki chodzi
# for chunk in about_talk_doc.noun_chunks:
#     print(chunk)


# Named Entity Recognition
## Znajdowanie nazwanych obiektów w tekście
### Własność ent pozwala nam na wyszukanie różnych atrybutów w tekście. Użyte w przykładzie poniżej:
#
# piano_class_text = ('Akademia Piano jest usytuowana'
#                     ' w Lublinie lub w mieście Warszawa i ma'
#                     ' światowej klasy instruktorów pianina.')
# piano_class_doc = nlp(piano_class_text)
# for ent in piano_class_doc.ents:
#     print(ent.text, ent.start_char, ent.end_char,
#           ent.label_, spacy.explain(ent.label_))

# displacy.serve(piano_class_doc, style='ent')

survey_text = ('Spośród 5 ankietowanych osób, Paweł Michciński,'
               ' Jan Kowalski i Andrzej Nowak lubią'
               ' jabłka. Anna Nowak i Mariola Kowalska'
               ' lubią pomarańcze.')


def replace_person_names(token):
    if token.ent_iob != 0 and token.ent_type_ == 'PERSON':
        return '[REDACTED] '
    return token.string


def redact_names(nlp_doc):
    for ent in nlp_doc.ents:
        ent.merge()
    tokens = map(replace_person_names, nlp_doc)
    return ''.join(tokens)


survey_doc = nlp(survey_text)
print(redact_names(survey_doc))

