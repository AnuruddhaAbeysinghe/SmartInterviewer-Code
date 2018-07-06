import random,time
import ConnectionToNeo4j,TextToSpeechConverter,QuestionCreator

from gingerit.gingerit import GingerIt
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




technology_list = []


def generate_cv_questions():
    db = "CV"
    # node_Count = ConnectionToNeo4j.getNodeCount(db)
    lang = 'en'
    q_list = []
    count = 1
    session = 0

    while count<=3:
        session = session + 1
        print("session")
        print(session)
        session_no_string = str(session)
        session_node_count = ConnectionToNeo4j.session_Node_Count(session_no_string)
        print("this is ")
        print(session_node_count)
        node_id = ConnectionToNeo4j.get_node_id(session_no_string)

        for id in range(node_id,session_node_count+node_id):
            q_list.append(str(id))
        print(q_list)

        print("node_count")
        print(session_node_count)
        for question_no in range(session_node_count):
            print("question number")
            print(question_no)
            random_que = random.choice(q_list)
            print("random que")
            print(random_que)



            non_technical_question = ConnectionToNeo4j.cvQuestionGen(random_que)
            q_list.remove(random_que)
            print(q_list)
            print(non_technical_question)
            actual_question = QuestionCreator.gen_Question(non_technical_question)
            parser = GingerIt()
            grammer_corrected_question_list = parser.parse(actual_question)
            grammer_corrected_question = grammer_corrected_question_list.get("result")
            TextToSpeechConverter.text_to_speech(grammer_corrected_question, lang)
            if random_que=="6":
                tech = input()
                global  technology_list
                technology_list = tech

        q_list = []
        count = count+1



#
# node_Count = ConnectionToNeo4j.getNodeCount(db)

# process_content()
# print((word, tag)for word, tag in sentence if tag in ('NN', 'JJ'))



