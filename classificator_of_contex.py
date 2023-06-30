import spacy
import load_save_classificator

if __name__ == '__main__':
   nlp = load_save_classificator.load('ru2_combined_400ks_96')
   spacy.explain("Degree")
   doc = nlp("Здраствуйте, я хочу купить 'Парацетамол', Россия, Москва")
   for word in doc:
      print(word.text, word.tag_, spacy.explain(word.tag_))






