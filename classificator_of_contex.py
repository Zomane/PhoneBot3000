import spacy


if __name__ == '__main__':
   nlp = spacy.load('ru2_combined_400ks_96')
   spacy.explain("Degree")
   doc = nlp("Здраствуйте, я хочу купить 'Парацетамол', Россия, Москва")
   for word in doc:
      print(word.text, word.tag_, spacy.explain(word.tag_))






