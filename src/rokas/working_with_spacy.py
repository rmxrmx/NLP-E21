import spacy
from typing import List
import os

nlp = spacy.load("en_core_web_sm")
doc = nlp("This is an English text")
print(type(doc))

token = doc[1]

print(dir(doc))


def corpus_loader(folder: str) -> List[str]:
    """
    A corpus loader function which takes in a path to a
    folder and returns a list of strings.
    """
    text_list = []
    for file in os.listdir(folder):
        read_file = open(os.path.join(folder, file), 'r')
        text_list.append(read_file.read())
        read_file.close()
    return text_list


training_path = os.path.join("..", "..", "syllabus", "classes", "data", "train_corpus")
print(corpus_loader(training_path))
