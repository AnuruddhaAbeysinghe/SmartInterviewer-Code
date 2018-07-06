import nltk
import sys
import nltk
import re
import time
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
sys.path.insert(0, '../Database')
import random,time
import ConnectionToNeo4j,TextToSpeechConverter
import TechnicalQuestionDictionary
from nltk.stem import WordNetLemmatizer
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
a={}
b=[]
train_text = state_union.raw("2005-GWBush.txt")
keywords ="multiple inheritance"


question = ""





# def gen_Question():
#     # if type(sentence) is str
#     db = "CV"
#     node_Count = ConnectionToNeo4j.getNodeCount(db)
#     lang = 'en'
#     q_list = []
#     for id in range(1,node_Count+1):
#         q_list.append(str(id))
#     print(q_list)
#
#     # process_content()
#     # print((word, tag)for word, tag in sentence if tag in ('NN', 'JJ'))
#
#



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
        print(key)
        print(words)
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

    if all(([key in words for key in TechnicalQuestionDictionary.tl1])):
        question = "What is a "+ keywords
        print(question)
    elif all([key in words for key in  TechnicalQuestionDictionary.tl2]):
        question = "Can you explain "+ keywords
        print(question)
    elif all([key in words for key in TechnicalQuestionDictionary.tl3]):
        question = "Describe about "+ keywords
        print(question)
    elif all([key in words for key in TechnicalQuestionDictionary.tl4]):
        question = "What is a "+ keywords
        print(question)
    elif all([key in words for key in TechnicalQuestionDictionary.tl5]):
        question = "What is a "+ keywords
        print(question)
    elif all([key in words for key in TechnicalQuestionDictionary.tl16]):
        question = "What is a "+ keywords
        print(question)
    elif all([key in words for key in TechnicalQuestionDictionary.tl7]):
        question = "What is "+ keywords
        print(question)
    elif all([key in words for key in TechnicalQuestionDictionary.tl8]):
        question = "What is a "+ keywords
        print(question)
    elif all([key in words for key in TechnicalQuestionDictionary.tl9]):
        question = "What is a "+ keywords
        print(question)
    elif all([key in words for key in TechnicalQuestionDictionary.tl10]):
        question = "What is "+ keywords
        print(question)
    elif all([key in words for key in TechnicalQuestionDictionary.tl11]):
        question = "What is a "+ keywords
        print(question)
    elif all([key in words for key in TechnicalQuestionDictionary.tl12]):
        question = "What is a "+ keywords
        print(question)
    elif all([key in words for key in TechnicalQuestionDictionary.tl13]):
        question = "What is a "+ keywords
        print(question)
    else:
        question = "Define about " + keywords
        print(question)

    return question


# gen_Question(keywords)