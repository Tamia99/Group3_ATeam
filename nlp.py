import os
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import questions
import robot
import re

stopwords = set()
porter_stemmer = PorterStemmer()
def readStopword():
    path = os.path.join('files','stopwords.txt')
    with open (path, 'r') as f:
        for line in f:
            stopwords.add(line.rstrip())

numberDic = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
}

def word_to_number(data):
    punctuation = '!,;:?"\'、，；'
    data = re.sub(r'[{}]+'.format(punctuation),' ',data)
    sep = re.split(r'million|billion|thousand', data)
    print(sep)
    result = []
    for s in sep:
        s = s.replace('and', '')
        s = s.strip()
        count = 0
        words = re.split('[ -]', s)
        print(words)
        res = []
        for word in words:
            if word in numberDic:
                count += numberDic[word]
            elif word == 'hundred':
                if count == 0:
                    count += 100
                else:
                    count = count * 100
            else:
                res.append(word)
        if words[0] in numberDic:
            res.insert(0, count)
        else:
            res.append(count)
        print(res)
        result.append(res)
    print(result)
    final = ''
    for r in result:
        for i in r:
            if isinstance(i,int):
                final += str(i)
            else:
                if i != '':
                    final = final + ' ' + i + ' '
    return final

def preprocessing(data):
    if len(stopwords) == 0:
        readStopword()
    data = data.lower().strip()
    data = word_to_number(data)
    print(data)
    words = []
    tags = pos_tag(word_tokenize(data))
    wnl = WordNetLemmatizer()
    for w, t in tags:
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
            process1 += 1
            process2 = 0
            returnlist = [questions.questionList[2], process1, process2]
        else:
            if len(set(wordsList).intersection(set(answerkeyword2))) != 0:
                process1 = -1
                process2 = -1
                returnlist = [questions.questionList[1], process1, process2]
            else:
                process2 += 1
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[0], process1, process2]
    # elif process1 == 1:
    #
    return returnlist


