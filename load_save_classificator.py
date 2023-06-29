import spacy
import ru_core_news_lg


def load(*args):
    spacy.load(*args)
    return ru_core_news_lg.load()


def save(nlp, *args):
    nlp.to_disk(*args)
