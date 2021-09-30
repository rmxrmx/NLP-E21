from collections import Counter
from typing import List
from datasets import load_dataset

# load the sst2 dataset
dataset = load_dataset("glue", "sst2")

# select the train split
train = dataset["train"]

print("Examining train set:")
print(train)
print(train.features)

print("Information about the dataset:")
print(train.info.description)
print("Homepage")
print(train.info.homepage)

print("Examining sentence")
print(type(train["sentence"]))
print(type(train["sentence"][0]))

print("Examining label")
print(type(train["label"]))
print(type(train["label"][0]))
# set takes all the unique values
print(set(train["label"]))

print("A few samples:")
for t in range(10):
    sent = train["sentence"][t]
    lab = train["label"][t]
    print(sent, "-", lab)


def term_freq(tokens: List[str]) -> dict:
    """
    Takes in a list of tokens (str) and return a dictionary of term frequency of each token
    """
    freq = dict(Counter(tokens))
    return {k: freq[k] / len(tokens) for k in freq}


def doc_freq(documents: List[List[str]]) -> dict:
    """
    Takes in a list of documents which each is a list of tokens and return a dictionary of frequencies for each token over all the documents. E.g. {"Aarhus": 20, "the": 2301, ...}
    """
    # c = Counter()
    # for l in documents:
    #     c.update(l)
    #
    # return dict(c)
    #
    # alternative implementation
    c = {}
    for l in documents:
        l_set = set(l)
        for key in l_set:
            if key in c:
                c[key] += 1
            else:
                c[key] = 1
    return c


print(term_freq(["testing", "these", "tokens", "these"]))
print(doc_freq([["testing", "these", "these", "tokens"], ["are", "these", "tokens", "working", "?"]]))