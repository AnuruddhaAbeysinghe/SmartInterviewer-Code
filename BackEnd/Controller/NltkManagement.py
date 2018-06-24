from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def NltlCalling(sentenceForNltk):

    sentence = sentenceForNltk
    stopWords = set(stopwords.words('english'))

    words = word_tokenize(sentence)
    wordsFiltered = []

    for w in words:
        if w not in stopWords:
            if (w!="I" and w!="old" and w!="years" and w!="followed" and w!="studying" and w!="My" and w!="weakness" and w!="strength" and w!="degree" and w!="used" and w!="GPA"):
                wordsFiltered.append(w)


    final_word = ""

    for word in wordsFiltered:
        final_word = final_word+" "+word
    print(final_word.lstrip())

    return final_word.lstrip()





