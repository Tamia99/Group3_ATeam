import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import tags
import robot

stopwords = set()
porter_stemmer = PorterStemmer()
def readStopword():
    path = os.path.join('files','stopwords.txt')
    with open (path, 'r') as f:
        for line in f:
            stopwords.add(line.rstrip())

def preprocessing(data):
    if len(stopwords) == 0:
        readStopword()
    words = word_tokenize(data)
    wordsList = []
    for w in words:
        w = w.lower()
        if w not in stopwords:
            w = porter_stemmer.stem(w)
            for items in tags.word:
                for i in items["key"]:
                    i = i.lower()
                    i = porter_stemmer.stem(i)
                    if w == i:
                        return items["value"]
            wordsList.append(w)
    return robot.getRespond(data)


