import spacy
from typing import List
import os
from collections import Counter

nlp = spacy.load("en_core_web_sm")
doc = nlp("This is an English text")


# print(dir(doc))


def corpus_loader(folder: str) -> List[str]:
    """
    A corpus loader function which takes in a path to a
    folder and returns a list of strings.
    """
    text_list = []
    for file in os.listdir(folder):
        with open(os.path.join(folder, file), 'r') as of:
            text_list.append(of.read())
    return text_list


def should_lemmatize(token):
    types = ["VERB", "ADJ", "NOUN"]
    if token.pos_ in types:
        return True
    return False


def lemmatize_text(text):
    new_text = ""
    doc = nlp(text)
    for token in doc:
        if should_lemmatize(token):
            new_text += token.lemma_ + " "
    return new_text


def text_to_pos(text):
    parts = ""
    doc = nlp(text)
    for token in doc:
        parts += token.pos_ + " "
    return parts


def calculate_pos(text):
    parts = text_to_pos(text)
    c = Counter(parts.split())
    return c


training_path = os.path.join("..", "..", "syllabus", "classes", "data", "train_corpus")
loaded_corpus = corpus_loader(training_path)


def calculate_mdd(text):
    t_sum = 0
    t_size = 0
    doc = nlp(text)
    for idx, token in enumerate(doc):
        for idx2, ft in enumerate(doc):
            if ft == token.head:
                dist = abs(idx - idx2)
                break

        t_sum += dist
        if dist != 0:
            t_size += 1

    mdd = t_sum / t_size
    return mdd


print(calculate_mdd(loaded_corpus[0]))
