
import sys

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
sys.path.insert(0, '../Database')



from BackEnd.Database import TechnicalQuestionDictionary

a={}
b=[]
train_text = state_union.raw("2005-GWBush.txt")
keywords ="multiple inheritance"


question = ""


def gen_Question(keywords):
    global question
    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    tokenized = custom_sent_tokenizer.tokenize(keywords)
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # print(tagged)
            # namedEnt = nltk.ne_chunk(tagged, binary=True)
            # gen_Question(namedEnt)
            # namedEnt.draw()


        key, words = zip(*tagged)
        #print(key)

        compare = list(words)
        print(words)
        print(compare)
        a = dict(zip(key, words))
        b= dict(zip(words, key))

        print(a)
        print("hey")
        # print([b for b, v in a.items() if v in l1])




    except Exception as e:
        print(str(e))

# print("bfehbgrhejrngr")
# print(TechnicalQuestionDictionary.tl1)
# print("bfehbgrhejrngr")

    if compare == TechnicalQuestionDictionary.tl1:
        question = "What is a "+ keywords
        print(question)
    elif compare ==   TechnicalQuestionDictionary.tl2:
        question = "Can you explain "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl3:
        question = "Describe about "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl4:
        question = "What is a "+ keywords
        print(question)
    elif compare == TechnicalQuestionDictionary.tl5:
        question = "What are "+ keywords
        print(question)
    elif compare == TechnicalQuestionDictionary.tl6:
        question = "What is a "+ keywords
        print(question)
    elif compare == TechnicalQuestionDictionary.tl7:
        question = "What are "+ keywords
        print(question)
    # elif compare == TechnicalQuestionDictionary.tl8:
    #     question = "What are "+ keywords
    #     print(question)
    elif compare == TechnicalQuestionDictionary.tl9:
        question = "What is a "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl10:
        question = "What are "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl11:
        question = "What is a "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl12:
        question = "How to use"+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl13:
        question = "What is a "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl14:
        question = "Describe about "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl15:
        question = "Describe about "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl16:
        question = "Describe about "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl17:
        question = "Tell about "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl18:
        question = "Explain about "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl19:
        question = "Describe "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl20:
        question = "What is a "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl21:
        question = "Describe about "+ keywords
        print(question)
    elif compare ==  TechnicalQuestionDictionary.tl22:
        question = "Tell about "+ keywords
        print(question)
    else:
        question = "Define about " + keywords
        print(question)

    return question