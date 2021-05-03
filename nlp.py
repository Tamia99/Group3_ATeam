import os
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import questions
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
    words = []
    tags = pos_tag(word_tokenize(data))
    wnl = WordNetLemmatizer()
    for w, t in tags:
        w = w.lower()
        # if w not in stopwords:
        if t.startswith('NN'):
            words.append(wnl.lemmatize(w, pos='n'))
        elif t.startswith('VB'):
            words.append(wnl.lemmatize(w, pos='v'))
        elif t.startswith('JJ'):
            words.append(wnl.lemmatize(w, pos='a'))
        elif t.startswith('R'):
            words.append(wnl.lemmatize(w, pos='r'))
        else:
            words.append(w)
    return words

def NaturalLanguageProcess(data, process1, process2):
    wordsList = preprocessing(data)
    print(wordsList)
    if process1 == 0:
        answerkeyword1 = ['yes','y','ok','yep','sure','yea','yeah','fine','okay']
        answerkeyword2 = ['no','n','never','noway']
        if len(set(wordsList).intersection(set(answerkeyword1))) != 0:
            print("1")
            process1 += 1
            process2 = 0
            returnlist = [questions.questionList[2], process1, process2]
        else:
            if len(set(wordsList).intersection(set(answerkeyword2))) != 0:
                print("2")
                process1 = -1
                process2 = -1
                returnlist = [questions.questionList[1], process1, process2]
            else:
                print("3")
                process2 += 1
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[0], process1, process2]
        return returnlist


