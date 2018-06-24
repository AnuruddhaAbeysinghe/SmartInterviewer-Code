import os
import time
from xml.etree import ElementTree
import TextToSpeechConverter
import random
from BackEnd.Controller import SpeachToText


lang = 'en'
result = 1
file_name = '../Database/CvQuestions.xml'

dom = ElementTree.parse(file_name)

starting_question = dom.find('Session[@name="Start"]/Question/Q')
starting_question_text = starting_question.text
TextToSpeechConverter.text_to_speech(starting_question_text,lang)
print (starting_question_text)

session1_questions = dom.findall('Session[@name="One"]/Question/Q')
# answer = input()

answer = SpeachToText.validation(starting_question_text)
print(answer)
if answer != result:
    # answer = input()
    answer = SpeachToText.validation(starting_question_text)
    print(answer)
    # time.sleep(500000)

for c in session1_questions:
    if answer == result:
        time.sleep(5)
        session1_questions_text = c.text
        TextToSpeechConverter.text_to_speech(session1_questions_text, lang)
        print(c.text)
        # answer = input()
        # print(c.text)
        answer = SpeachToText.validation(session1_questions_text)
        print(answer)

    while answer != result:
        # answer = input()
        time.sleep(5)
        answer = SpeachToText.validation(session1_questions_text)
        print(answer)
        # time.sleep(0)

session2_question = dom.findall('Session[@name="Two"]/Question/Q')

question_list=[]
for q in session2_question:
    question_list.append(q.text)
for pri in range(2):
    if answer == result:
        time.sleep(5)
        random_question = random.choice(question_list)
        TextToSpeechConverter.text_to_speech(random_question, lang)
        print(random_question)
        # answer = input()
        answer = SpeachToText.validation(random_question)
        print(answer)
        question_list.remove(random_question)

    while answer != result:
        # answer = input()
        time.sleep(5)
        answer = SpeachToText.validation(random_question)
        print(answer)
        # time.sleep(0)



session3_questions = dom.findall('Session[@name="Three"]/Question/Q')
if answer != result:
    time.sleep(5)
    # answer = input()
    answer = SpeachToText.validation(random_question)
    print(answer)
    # time.sleep(0)

for c in session3_questions:
    if answer == result:
        time.sleep(5)
        session3_questions_text = c.text
        TextToSpeechConverter.text_to_speech(session3_questions_text, lang)
        print(c.text)
        # answer = input()
        answer = SpeachToText.validation(c.text)
        print(answer)


    while answer != result:
        time.sleep(5)
        # answer = input()
        answer = SpeachToText.validation(c.text)
        print(answer)
        # time.sleep(0)



















