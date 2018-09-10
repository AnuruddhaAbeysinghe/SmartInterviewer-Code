import speech_recognition as sr
from BackEnd.Controller import ConnectionToNeo4j, MostRecentAudioFileAccess, AnswerValidating


def validation(subsection, typer, treetype,qno):
 r = sr.Recognizer()
 audio = "../Audio/"+MostRecentAudioFileAccess.MostRecentAudioClip()
 marks = "No"

 with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print('Loading..')
 try:
    text = r.recognize_google(audio)
    print(text)

    if typer == "technical":
        valuefromdb = ConnectionToNeo4j.getValueFromdb(subsection, treetype)
        marks = AnswerValidating.ValidatingTechnical(text, valuefromdb,qno)
    if typer == "nontechnical":
        marks = AnswerValidating.ValidatingNonTechnical(text,qno)
 except Exception as e:
    print(e)
 return marks
