import spacy

if __name__ == '__main__':
   nlp = spacy.load('ru_core_news_lg')
   import ru_core_news_lg
   nlp = ru_core_news_lg.load()
   spacy.explain("Degree")
   doc = nlp("Здраствуйте, я хочу купить 'Парацетамол', Россия, Москва")
   for word in doc:
      print(word.text, word.tag_, spacy.explain(word.tag_))






