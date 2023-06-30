import spacy
from spacy.tokens import Doc, DocBin

nlp = spacy.blank("ru")
docbin = DocBin()
words = ["Apple", "is", "looking", "at", "buying", "U.K.", "startup", "."]
spaces = [True, True, True, True, True, True, True, False]
ents = ["B-ORG", "O", "O", "O", "O", "B-GPE", "O", "O"]
doc = Doc(nlp.vocab, words=words, spaces=spaces, ents=ents)
docbin.add(doc)
docbin.to_disk("./train.spacy")





