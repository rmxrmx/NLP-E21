import os
import re


class Corpus:
    def __init__(self, train_path):
        self.corpus_list = []
        self.load_text(train_path)
        self.segment_text()

    def load_text(self, train_path):
        for file in os.listdir(train_path):
            read_file = open(os.path.join(train_path, file), 'r')
            self.corpus_list.append(CorpusText(int(file[:-4]), read_file.read(), None, None))
            read_file.close()

    def segment_text(self):
        for c_text in self.corpus_list:
            text = c_text.text

            sentences = re.split(r'[.|?|!]', text)

            c_text.sentences = sentences


class CorpusText:
    def __init__(self, identity, text, tokenization, sentences):
        self.id = identity
        self.text = text
        self.tokenization = tokenization
        self.sentences = sentences


training_path = os.path.join("..", "..", "syllabus", "classes", "class2", "train_corpus")
c = Corpus(training_path)
