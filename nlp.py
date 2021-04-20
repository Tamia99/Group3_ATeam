import os
import nltk
from nltk.tokenize import word_tokenize

stopwords = set()
def readStopword():
    path = os.path.join('files','stopwords.txt')
    with open (path, 'r') as f:
        for line in f:
            stopwords.add(line.rstrip())

def preprocessing():
    readStopword()
    data = "All work and no play makes jack a dull boy, all work and no play"
    words = word_tokenize(data)
    wordsList = []
    for w in words:
        if w not in stopwords:
            wordsList.append(w)
    return wordsList


