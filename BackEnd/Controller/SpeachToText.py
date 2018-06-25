import speech_recognition as sr
from BackEnd.Controller import ConnectionToNeo4j, NltkManagement


def validation(question):
 r = sr.Recognizer()
 lable = ""
 audio = ""
 if question == "What is your name?":
     lable = "name"
     audio = '../Audio/question 1.wav'

 if question == "How old are you?":
     lable = "age"
     audio = '../Audio/question 2.wav'

 if question == "What is your School?":
     lable = "School"
     audio = '../Audio/question 3.wav'

 if question == "What is the stream that you follow for Advanced Level?":
     lable = "AL"
     audio = '../Audio/question 4.wav'

 if question == "What is your university?":
     lable = "university"
     audio = '../Audio/question 5.wav'

 if question == "What are your weaknesses?":
     lable = "weaknesses"
     audio = '../Audio/question 6.wav'

 if question == "What are your Strengths?":
     lable = "Strengths"
     audio = '../Audio/question 7.wav'

 if question == "Why should we hire you?":
     lable = "why"
     audio = '../Audio/question 8.wav'

 if question == "what is your recent education qualification?":
     lable = "qualification"
     audio = '../Audio/question 9.wav'

 if question == "what are the projects that you did?":
     lable = "project"
     audio = '../Audio/question 10.wav'

 if question == "what are the technologies that you have used?":
     lable = "technology"
     audio = '../Audio/question 11.wav'
 if question == "what is your gpa?":
     lable = "GPA"
     audio = '../Audio/question 12.wav'


 with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print('Done!')
 try:
    text = r.recognize_google(audio)
    print(text)
    exist = ConnectionToNeo4j.validationAnswer(NltkManagement.NltlCalling(text), lable)
 except Exception as e:
    print(e)
 return exist