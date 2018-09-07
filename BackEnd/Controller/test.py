from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from BackEnd.Controller import WeightOfTheAnswer



def ValidatingTechnical():

    sentence1 = "accepts any python object and converts it into a string representation and dumps it into a file by using dump function"
    sentence2 = "accepts any python object and converts it into a string representation and dumps it into a file by using dump function"

    grammarMarks = WeightOfTheAnswer.process_content(sentence1)

    if len(sentence1.split()) == 0:
        return None

    else:

        stopWords = set(stopwords.words('english'))

        words1 = word_tokenize(sentence1)
        words2 = word_tokenize(sentence2)

        wordsFiltered1 = []
        wordsFiltered2 = []

        for w in words1:
            if w not in stopWords:
                wordsFiltered1.append(w)

        for w in words2:
            if w not in stopWords:
                wordsFiltered2.append(w)

        marks = 0
        final_word = ""

        for word2 in wordsFiltered2:
            for word1 in wordsFiltered1:
                if word2 == word1:
                    marks+= 1

        for word in wordsFiltered2:
            final_word = final_word+" "+word

        wordcountofdbanswer = len(final_word.split())
        print(marks)
        print(wordcountofdbanswer)
        finalmark = (marks/wordcountofdbanswer)+grammarMarks

        # finalmark = SequenceMatcher(None, wordsFiltered1, wordsFiltered2).ratio()

        return "%.2f" % finalmark

def ValidatingNonTechnical(answer):

    answerwordcount = len(answer.split())

    if answerwordcount == 0:
        return None
    if answerwordcount < 15:
        return  0.5
    if answerwordcount > 15:
        return 1