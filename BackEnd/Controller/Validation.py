from BackEnd.Controller import SpeachToText

def func():
    q="java  overriding object  technical"

    # subsection = input("enter sub area : \n")
    # typer = input("enter type : \n")pickling
    value = SpeachToText.validation("pickling", "technical")
    #print("correctnessof the answer:"+value)
    return value
