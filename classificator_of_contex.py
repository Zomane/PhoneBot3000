import spacy


if __name__ == '__main__':
   nlp = spacy.blank('ru').from_disk('ru2_combined_400ks_96')
   import ru2_combined_400ks_96
   nlp = ru2_combined_400ks_96.load()
   spacy.explain("Degree")
   doc = nlp("Здраствуйте, я хочу купить 'Парацетамол', Россия, Москва")
   for word in doc:
      print(word.text, word.tag_, spacy.explain(word.tag_))






