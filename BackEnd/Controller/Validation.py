from BackEnd.Controller import SpeachToText

q1 = "What is your name?"
q2 = "How old are you?"
q3 = "What is your School?"
q4 = "What is the stream that you follow for Advanced Level?"
q5 = "What is your university?"
q6 = "What are your weaknesses?"
q7 = "What are your Strengths?"
q8 = "Why should we hire you?"
q9 = "what is your recent education qualification?"
q10 = "what are the projects that you did?"
q11= "what are the technologies that you have used?"
q12 = "what is your gpa?"

test = input("enter question : \n")

value = SpeachToText.validation(test)
print(value)
