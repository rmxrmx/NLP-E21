import spacy
from typing import List
import os

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


training_path = os.path.join("..", "..", "syllabus", "classes", "data", "train_corpus")
loaded_corpus = corpus_loader(training_path)

# lemmatize texts
# for idx, text in enumerate(loaded_corpus[:20]):
#     lemmatized = lemmatize_text(text)
#     loaded_corpus[idx] = lemmatized
#
# print(loaded_corpus[0])

