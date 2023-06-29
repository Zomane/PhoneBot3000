import spacy
from spacy.symbols import ORTH, TAG

nlp = spacy.load("ru_core_news_lg")

# Добавляем новый тег в словарь тегов
nlp.vocab.morphology.add_special_case("мое_слово", [{ORTH: "мое_слово", TAG: "МОЙ_ТЕГ"}])

doc = nlp("Это пример текста с моим словом.")
for token in doc:
    print(token.text, token.tag_, token.pos_)