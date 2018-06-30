from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



def ValidatingTechnical(userAnswer, dbAnswer):

    sentence1 = userAnswer
    sentence2 = dbAnswer

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

        for word in wordsFiltered1:
            final_word = final_word+" "+word


        print(marks)

        wordcountofdbanswer = len(final_word.split())
        print(wordcountofdbanswer)
        finalmark = marks/wordcountofdbanswer

        return "%.2f" % finalmark

def ValidatingNonTechnical(answer):

    answerwordcount = len(answer.split())

    if answerwordcount == 0:
        return None
    if answerwordcount < 15:
        return  0.5
    if answerwordcount > 15:
        return 1