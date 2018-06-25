import random,time
import ConnectionToNeo4j,TextToSpeechConverter

def question_generator ():
    lang = 'en'
    q_list = []
    for id in range(1,5):
        q_list.append(str(id))

    print(q_list)

    for question_no  in range(4):
        time.sleep(5)
        random_que = random.choice(q_list)
        technical_question=ConnectionToNeo4j.ontologyQuestionGen(random_que)
        q_list.remove(random_que)
        actual_question = "What is "+technical_question+"?"
        TextToSpeechConverter.text_to_speech(actual_question, lang)
        print(actual_question)
