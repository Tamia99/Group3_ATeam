import os
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import questions
import robot
import re
import recommendation
import database

stopwords = set()
porter_stemmer = PorterStemmer()
def readStopword():
    path = os.path.join('files','stopwords.txt')
    with open (path, 'r') as f:
        for line in f:
            stopwords.add(line.rstrip())
informationlist = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', -1, -1, -1, -1, -1, -1, -1, '', '', '']

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
    sep = re.split(r'million|billion|thousand|millions|billions|thousands', data)
    result = []
    for s in sep:
        s = s.replace('and', '')
        s = s.strip()
        words = re.split('[ -]', s)
        # print('word to number: ')
        # print(words)
        res = []
        for word in words:
            if word in numberDic:
                count = 0
                break
            elif word == 'hundred' or word == 'hundreds':
                count = 0
                break
            else:
                count = ''

        for word in words:
            if word in numberDic:
                count += numberDic[word]
            elif word == 'hundred' or word == 'hundreds':
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
        result.append(res)
    final = ''
    for r in result:
        # print(r)
        for i in r:
            if isinstance(i,int):
                # print(i)
                # print(len(str(i)))
                if len(str(i)) == 1:
                    final = final + '00' + str(i)
                elif len(str(i)) == 2:
                    final = final + '0' + str(i)
                else:
                    final += str(i)
            else:
                if i != '':
                    final = final + ' ' + i + ' '
    return final

def preprocessing(data):
    if len(stopwords) == 0:
        readStopword()
    data = word_to_number(data)
    # print('preprocessing: ')
    # print(data)
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
    data = data.lower().strip()
    wordsList = preprocessing(data)
    # print('nature: ')
    # print(wordsList)
    # print(process1)
    # print(process2)
    if process1 == -1:
        returnlist = [robot.getRespond(data), process1, process2]
    elif process1 == 0:
        answerkeyword1 = ['yes','y','ok','yep','sure','yea','yeah','fine','okay','maybe','need','of course','get']
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
    elif process1 == 1:
        i = 0
        for word in wordsList:
            if word.isdigit():
                if int(word) < 10000000 and int(word) > 20000:
                    process1 = 2
                    process2 = 0
                    informationlist[24] = word
                    returnlist = ["Ok, I know. Let's come to next question." + '\n' + questions.questionList[3], process1, process2]
                else:
                    if process2 == 0:
                        # print('test')
                        process2 = 1
                        informationlist[24] = ''
                        returnlist = ['Umm..., your answer seems unreasonable, please check it again' + '\n' + questions.questionList[2], process1, process2]
                    elif process2 == 1:
                        process2 = 0
                        process1 = 2
                        informationlist[24] = ''
                        returnlist = ['Umm..., your answer seems unreasonable, let me change another question.' + '\n' + questions.questionList[3], process1, process2]
            else:
                i += 1
        if (i == len(wordsList)):
            if process2 == 0:
                # print('test')
                process2 = 1
                informationlist[24] = ''
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[2], process1, process2]
            elif process2 == 1:
                process2 = 0
                process1 = 2
                informationlist[24] = ''
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[3], process1, process2]

    elif process1 == 2:
        i = 0
        for word in wordsList:
            if word.isdigit():
                if int(word) < 15 and int(word) >= 0:
                    process1 = 3
                    process2 = 0
                    informationlist[17] = word
                    returnlist = ["I see." + '\n' + questions.questionList[4], process1, process2]
                else:
                    if process2 == 0:
                        # print('test')
                        process2 = 1
                        informationlist[17] = -1
                        returnlist = ['Umm..., your answer seems unreasonable, please check it again' + '\n' + questions.questionList[3], process1, process2]
                    elif process2 == 1:
                        process2 = 0
                        process1 = 3
                        informationlist[17] = -1
                        returnlist = ['Umm..., your answer seems unreasonable, let me change another question.' + '\n' + questions.questionList[4], process1, process2]
            else:
                i += 1
        if (i == len(wordsList)):
            if process2 == 0:
                # print('test')
                process2 = 1
                informationlist[17] = -1
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[3], process1, process2]
            elif process2 == 1:
                process2 = 0
                process1 = 3
                informationlist[17] = -1
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[4], process1, process2]
    elif process1 == 3:
        i = 0
        for word in wordsList:
            if word.isdigit():
                if int(word) < 10 and int(word) >= 0:
                    process1 = 4
                    process2 = 0
                    informationlist[15] = word
                    returnlist = ["Ok." + '\n' + questions.questionList[5], process1, process2]
                else:
                    if process2 == 0:
                        # print('test')
                        process2 = 1
                        informationlist[15] = -1
                        returnlist = ['Umm..., your answer seems unreasonable, please check it again' + '\n' + questions.questionList[4], process1, process2]
                    elif process2 == 1:
                        process2 = 0
                        process1 = 4
                        informationlist[15] = -1
                        returnlist = ['Umm..., your answer seems unreasonable, let me change another question.' + '\n' + questions.questionList[5], process1, process2]
            else:
                i += 1
        if (i == len(wordsList)):
            if process2 == 0:
                # print('test')
                process2 = 1
                informationlist[15] = -1
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[4], process1, process2]
            elif process2 == 1:
                process2 = 0
                process1 = 4
                informationlist[15] = -1
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[5], process1, process2]
    elif process1 == 4:
        i = 0
        for word in wordsList:
            if word.isdigit():
                if int(word) < 6 and int(word) >= 0:
                    process1 = 5
                    process2 = 0
                    informationlist[16] = word
                    returnlist = ["Well." + '\n' + questions.questionList[6], process1, process2]
                else:
                    if process2 == 0:
                        # print('test')
                        process2 = 1
                        informationlist[16] = -1
                        returnlist = ['Umm..., your answer seems unreasonable, please check it again' + '\n' + questions.questionList[5], process1, process2]
                    elif process2 == 1:
                        process2 = 0
                        process1 = 5
                        informationlist[16] = -1
                        returnlist = ['Umm..., your answer seems unreasonable, let me change another question.' + '\n' + questions.questionList[6], process1, process2]
            else:
                i += 1
        if (i == len(wordsList)):
            if process2 == 0:
                # print('test')
                process2 = 1
                informationlist[16] = -1
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[5], process1, process2]
            elif process2 == 1:
                process2 = 0
                process1 = 5
                informationlist[16] = -1
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[6], process1, process2]
    elif process1 == 5:
        i = 0
        for word in wordsList:
            if word.isdigit():
                if int(word) < 250000 and int(word) >= 1000:
                    process1 = 6
                    process2 = 0
                    informationlist[1] = word
                    returnlist = ["Well." + '\n' + questions.questionList[7], process1, process2]
                else:
                    if process2 == 0:
                        # print('test')
                        process2 = 1
                        informationlist[1] = ''
                        returnlist = ['Umm..., your answer seems unreasonable, please check it again' + '\n' + questions.questionList[6], process1, process2]
                    elif process2 == 1:
                        process2 = 0
                        process1 = 6
                        informationlist[1] = ''
                        returnlist = ['Umm..., your answer seems unreasonable, let me change another question.' + '\n' + questions.questionList[7], process1, process2]
            else:
                i += 1
        if (i == len(wordsList)):
            if process2 == 0:
                # print('test')
                process2 = 1
                informationlist[1] = ''
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[6], process1, process2]
            elif process2 == 1:
                process2 = 0
                process1 = 6
                informationlist[1] = ''
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[7], process1, process2]
    elif process1 == 6:
        ans = False
        answerlist = ['it does not matter', 'bloomington heights', 'bluestem', 'briardale', 'brookside',
                      'clear creek', 'college creek', 'crawford', 'edwards', 'gilbert', 'iowa dot and rail road',
                      'meadow village', 'mitchell', 'north ames', 'northridge', 'northpark villa', 'northridge heights',
                      'northwest ames', 'old town', 'south & west of iowa state university', 'sawyer', 'sawyer west',
                      'somerset', 'stone brook', 'timberland', 'veenker']
        item = ['-1', 'Blmngtn', 'Blueste', 'Brdale', 'Brkside', 'Clearcr',
                'Collgcr', 'Crawfor', 'Edwards', 'Gilbert', 'IDOTRR',
                'MeadowV', 'Mitchel', 'NAmes', 'NoRidge', 'NPkVill',
                'NridgHt', 'NWAmes', 'OldTown', 'SWISU', 'Sawyer',
                'SawyerW', 'Somerst', 'StoneBr', 'Timber', 'Veenker']
        for i,answer in enumerate(answerlist):
            if re.match(answer,data) is not None:
                process1 = 7
                process2 = 0
                informationlist[4] = item[i]
                returnlist = ["Well." + '\n' + questions.questionList[8], process1, process2]
                ans = True
                break
        if ans == False:
            i = 0
            for word in wordsList:
                if word.isdigit():
                    if int(word) <= 25 and int(word) >= 0:
                        process1 = 7
                        process2 = 0
                        informationlist[4] = item[int(word)]
                        returnlist = ["Well." + '\n' + questions.questionList[8], process1, process2]
                    else:
                        if process2 == 0:
                            # print('test')
                            process2 = 1
                            informationlist[4] = ''
                            returnlist = ['Umm..., your answer seems unreasonable, please check it again' + '\n' + questions.questionList[7], process1, process2]
                        elif process2 == 1:
                            process2 = 0
                            process1 = 7
                            informationlist[4] = ''
                            returnlist = ['Umm..., your answer seems unreasonable, let me change another question.' + '\n' + questions.questionList[8], process1, process2]
                else:
                    i += 1
            print(i)
            if (i == len(wordsList)):
                print('2')
                if process2 == 0:
                    # print('test')
                    process2 = 1
                    informationlist[4] = ''
                    returnlist = [robot.getRespond(data) + '\n' + questions.questionList[7], process1, process2]
                elif process2 == 1:
                    process2 = 0
                    process1 = 7
                    informationlist[4] = ''
                    returnlist = [robot.getRespond(data) + '\n' + questions.questionList[8], process1, process2]
    elif process1 == 7:
        ans = False
        item = ['-1', 'AllPub', 'NoSewr', 'NoSeWa', 'ELO']
        answerlist = ['it does not matter', 'all public utilities (e,g,w,& s)', 'electricity, gas, and water (septic tank)', 'electricity and gas only', 'electricity only']
        for i, answer in enumerate(answerlist):
            if re.match(answer.lower(),data) is not None:
                process1 = 8
                process2 = 0
                informationlist[3] = item[i]
                returnlist = ["Well." + '\n' + questions.questionList[9], process1, process2]
                ans = True
                break
        if ans == False:
            i = 0
            for word in wordsList:
                if word.isdigit():
                    if int(word) <= 4 and int(word) >= 0:
                        process1 = 8
                        process2 = 0
                        informationlist[3] = item[int(word)]
                        returnlist = ["Well." + '\n' + questions.questionList[9], process1, process2]
                    else:
                        if process2 == 0:
                            # print('test')
                            process2 = 1
                            informationlist[3] = ''
                            returnlist = ['Umm..., your answer seems unreasonable, please check it again' + '\n' + questions.questionList[8], process1, process2]
                        elif process2 == 1:
                            process2 = 0
                            process1 = 8
                            informationlist[3] = ''
                            returnlist = ['Umm..., your answer seems unreasonable, let me change another question.' + '\n' + questions.questionList[9], process1, process2]
                else:
                    i += 1
            if (i == len(wordsList)):
                if process2 == 0:
                    # print('test')
                    process2 = 1
                    informationlist[3] = ''
                    returnlist = [robot.getRespond(data) + '\n' + questions.questionList[8], process1, process2]
                elif process2 == 1:
                    process2 = 0
                    process1 = 8
                    informationlist[3] = ''
                    returnlist = [robot.getRespond(data) + '\n' + questions.questionList[9], process1, process2]
    elif process1 == 8:
        ans = False
        item = ['-1', '1Story', '1.5Fin', '1.5Unf', '2Story', '2.5Fin', '2.5Unf',
                'SFoyer', 'SLvl']
        answerlist = ['it does not matter', 'one story', 'one and one-half story: 2nd level finished', 'one and one-half story: 2nd level unfinished',
                      'two story', 'two and one-half story: 2nd level finished', 'two and one-half story: 2nd level unfinished', 'split foyer', 'split level']
        for i, answer in enumerate(answerlist):
            if re.match(answer.lower(),data) is not None:
                process1 = 9
                process2 = 0
                informationlist[5] = item[i]
                returnlist = ["Well." + '\n' + questions.questionList[10], process1, process2]
                ans = True
                break
        if ans == False:
            i = 0
            for word in wordsList:
                if word.isdigit():
                    if 8 >= int(word) >= 0:
                        process1 = 9
                        process2 = 0
                        informationlist[5] = item[int(word)]
                        returnlist = ["Well." + '\n' + questions.questionList[10], process1, process2]
                    else:
                        if process2 == 0:
                            # print('test')
                            process2 = 1
                            informationlist[5] = ''
                            returnlist = ['Umm..., your answer seems unreasonable, please check it again' + '\n' + questions.questionList[9], process1, process2]
                        elif process2 == 1:
                            process2 = 0
                            process1 = 9
                            informationlist[5] = ''
                            returnlist = ['Umm..., your answer seems unreasonable, let me change another question.' + '\n' + questions.questionList[10], process1, process2]
                else:
                    i += 1
            if (i == len(wordsList)):
                if process2 == 0:
                    # print('test')
                    process2 = 1
                    informationlist[5] = ''
                    returnlist = [robot.getRespond(data) + '\n' + questions.questionList[9], process1, process2]
                elif process2 == 1:
                    process2 = 0
                    process1 = 9
                    informationlist[5] = ''
                    returnlist = [robot.getRespond(data) + '\n' + questions.questionList[10], process1, process2]
    elif process1 == 9:
        ans = False
        item = ['-1', 'Floor', 'GasA', 'GasW', 'Grav', 'OthW', 'Wall']
        answerlist = ['It does not matter', 'Floor Furnace', 'Gas forced warm air furnace',
                      'Gas hot water or steam heat', 'Gravity furnace',
                      'Hot water or steam heat other than gas', 'Wall furnace']
        for i, answer in enumerate(answerlist):
            if re.match(answer.lower(),data) is not None:
                process1 = 10
                process2 = 0
                informationlist[11] = item[i]
                returnlist = ["Well." + '\n' + questions.questionList[11], process1, process2]
                ans = True
                break
        if ans == False:
            i = 0
            for word in wordsList:
                if word.isdigit():
                    if int(word) <= 6 and int(word) >= 0:
                        process1 = 10
                        process2 = 0
                        informationlist[11] = item[int(word)]
                        returnlist = ["Well." + '\n' + questions.questionList[11], process1, process2]
                    else:
                        if process2 == 0:
                            # print('test')
                            process2 = 1
                            informationlist[11] = ''
                            returnlist = ['Umm..., your answer seems unreasonable, please check it again' + '\n' +
                                          questions.questionList[10], process1, process2]
                        elif process2 == 1:
                            process2 = 0
                            process1 = 10
                            informationlist[11] = ''
                            returnlist = ['Umm..., your answer seems unreasonable, let me change another question.' + '\n' +
                                          questions.questionList[11], process1, process2]
                else:
                    i += 1
            if (i == len(wordsList)):
                if process2 == 0:
                    # print('test')
                    process2 = 1
                    informationlist[11] = ''
                    returnlist = [robot.getRespond(data) + '\n' + questions.questionList[10], process1, process2]
                elif process2 == 1:
                    process2 = 0
                    process1 = 10
                    informationlist[11] = ''
                    returnlist = [robot.getRespond(data) + '\n' + questions.questionList[11], process1, process2]
    elif process1 == 10:
        ans = False
        item = ['-1', 'Y', 'N']
        answerlist = ['It does not matter', 'Yes', 'No']
        for i, answer in enumerate(answerlist):
            if re.match(answer.lower(),data) is not None:
                process1 = 11
                process2 = 0
                informationlist[12] = item[i]
                returnlist = ["Well." + '\n' + questions.questionList[12], process1, process2]
                ans = True
                break
        if ans == False:
            i = 0
            for word in wordsList:
                if word.isdigit():
                    if int(word) <= 2 and int(word) >= 0:
                        process1 = 11
                        process2 = 0
                        informationlist[12] = item[int(word)]
                        returnlist = ["Well." + '\n' + questions.questionList[12], process1, process2]
                    else:
                        if process2 == 0:
                            # print('test')
                            process2 = 1
                            informationlist[12] = ''
                            returnlist = ['Umm..., your answer seems unreasonable, please check it again' + '\n' +
                                          questions.questionList[11], process1, process2]
                        elif process2 == 1:
                            process2 = 0
                            process1 = 11
                            informationlist[12] = ''
                            returnlist = ['Umm..., your answer seems unreasonable, let me change another question.' + '\n' +
                                          questions.questionList[12], process1, process2]
                else:
                    i += 1
            if (i == len(wordsList)):
                if process2 == 0:
                    # print('test')
                    process2 = 1
                    informationlist[12] = ''
                    returnlist = [robot.getRespond(data) + '\n' + questions.questionList[11], process1, process2]
                elif process2 == 1:
                    process2 = 0
                    process1 = 11
                    informationlist[12] = ''
                    returnlist = [robot.getRespond(data) + '\n' + questions.questionList[12], process1, process2]
    elif process1 == 11:
        i = 0
        for word in wordsList:
            if word.isdigit():
                if int(word) <= 5 and int(word) >= 0:
                    process1 = 12
                    process2 = 0
                    informationlist[18] = word
                    returnlist = ["Well." + '\n' + questions.questionList[13], process1, process2]
                else:
                    if process2 == 0:
                        # print('test')
                        process2 = 1
                        informationlist[18] = -1
                        returnlist = ['Umm..., your answer seems unreasonable, please check it again' + '\n' + questions.questionList[12], process1, process2]
                    elif process2 == 1:
                        process2 = 0
                        process1 = 12
                        informationlist[18] = -1
                        returnlist = ['Umm..., your answer seems unreasonable, let me change another question.' + '\n' + questions.questionList[13], process1, process2]
            else:
                i += 1
        if (i == len(wordsList)):
            if process2 == 0:
                # print('test')
                process2 = 1
                informationlist[18] = -1
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[12], process1, process2]
            elif process2 == 1:
                process2 = 0
                process1 = 12
                informationlist[18] = -1
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[13], process1, process2]
    elif process1 == 12:
        i = 0
        for word in wordsList:
            if word.isdigit():
                if int(word) <= 6 and int(word) >= 0:
                    process1 = 13
                    process2 = 0
                    informationlist[22] = word
                    returnlist = ["Well." + '\n' + questions.questionList[14], process1, process2]
                else:
                    if process2 == 0:
                        # print('test')
                        process2 = 1
                        informationlist[22] = ''
                        returnlist = ['Umm..., your answer seems unreasonable, please check it again' + '\n' + questions.questionList[13], process1, process2]
                    elif process2 == 1:
                        process2 = 0
                        process1 = 13
                        informationlist[22] = ''
                        returnlist = ['Umm..., your answer seems unreasonable, let me change another question.' + '\n' + questions.questionList[14], process1, process2]
            else:
                i += 1
        if (i == len(wordsList)):
            if process2 == 0:
                # print('test')
                process2 = 1
                informationlist[22] = ''
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[13], process1, process2]
            elif process2 == 1:
                process2 = 0
                process1 = 13
                informationlist[22] = ''
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[14], process1, process2]
    elif process1 == 13:
        i = 0
        for word in wordsList:
            if word.isdigit():
                if int(word) <= 15 and int(word) >= 0:
                    informationlist[20] = word
                    count = 0
                    for i in informationlist:
                        if i != '' and i != -1:
                            count += 1
                    if count >= 6:
                        process2 = 0
                        process1 = 14
                        returnlist = ['I see. Thank you for answering all the question.' + '\n' + questions.questionList[15], process1, process2]
                    else:
                        process2 = 0
                        process1 = 15
                        returnlist = ['Umm..., your answer seems unreasonable.' + '\n' + questions.questionList[16], process1, process2, informationlist]
                else:
                    if process2 == 0:
                        # print('test')
                        process2 = 1
                        informationlist[20] = -1
                        returnlist = ['Umm..., your answer seems unreasonable, please check it again' + '\n' + questions.questionList[14], process1, process2]
                    elif process2 == 1:
                        count = 0
                        for i in informationlist:
                            if i != '' and i != -1:
                                count += 1
                        if count >= 6:
                            process2 = 0
                            process1 = 14
                            informationlist[20] = -1
                            returnlist = ['Umm..., your answer seems unreasonable.' + '\n' + 'Above are all the question.' + questions.questionList[
                                    15], process1, process2]
                        else:
                            process2 = 0
                            process1 = 15
                            informationlist[20] = -1
                            returnlist = ['Umm..., your answer seems unreasonable.' + '\n' + questions.questionList[16], process1,
                                          process2, informationlist]
            else:
                i += 1
        if (i == len(wordsList)):
            if process2 == 0:
                # print('test')
                process2 = 1
                informationlist[20] = -1
                returnlist = [robot.getRespond(data) + '\n' + questions.questionList[14], process1, process2]
            elif process2 == 1:
                count = 0
                for i in informationlist:
                    if i != '' and i != -1:
                        count += 1
                if count >= 6:
                    process2 = 0
                    process1 = 14
                    informationlist[20] = -1
                    returnlist = [robot.getRespond(data) + '\n' + 'Above are all the question.' + questions.questionList[15], process1, process2]
                else:
                    process2 = 0
                    process1 = 15
                    informationlist[20] = -1
                    returnlist = [robot.getRespond(data) + '\n' + questions.questionList[16], process1, process2, informationlist]
    elif process1 == 14:
        answerkeyword1 = ['yes', 'y', 'ok', 'yep', 'sure', 'yea', 'yeah', 'fine', 'okay']
        # answerkeyword2 = ['no', 'n', 'never', 'noway']
        if len(set(wordsList).intersection(set(answerkeyword1))) != 0:
            process1 = 16
            process2 = 0
            returnlist = ['', process1, process2, informationlist]
        else:
            houselist = recommendation.recommendationSysAlgorithm(informationlist)
            houseinfo = database.getHouseByIds(houselist)
            process1 = 17
            process2 = 0
            returnlist = ['', process1, process2, houseinfo]
        print(informationlist)
    elif process1 == 15:
        returnlist = ['Please fill in the questionnaire and submit it, then we can recommend suitable houses for you.', process1, process2, informationlist]
    elif process1 == 16:
        process1 = 17
        process2 = 0
        houselist = recommendation.recommendationSysAlgorithm(informationlist)
        houseinfo = database.getHouseByIds(houselist)
        returnlist = ['', process1, process2, houseinfo]
    elif process1 == 17:
        process2 += 1
        returnlist = [robot.getRespond(data), process1, process2]

    # print(process1)
    # print(process2)
    print(informationlist)
    return returnlist


