import random,time
from BackEnd.Controller  import ConnectionToNeo4j,TextToSpeechConverter,QuestionCreator,NestedQuestionCreator,vari,test

from gingerit.gingerit import GingerIt
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




# technology_list = []
userid = vari.userId

def generate_cv_questions():
    db = "CV"
    # node_Count = ConnectionToNeo4j.getNodeCount(db)
    lang = 'en'
    q_list = []
    pro_list = []
    count = 1
    session = 0
    answer_validity = 0


    while count<=3:
        session = session + 1
        print("session")
        print(session)
        session_no_string = str(session)
        session_node_count = ConnectionToNeo4j.session_Node_Count(db,session_no_string)
        print("this is ")
        print(session_node_count)
        node_id = ConnectionToNeo4j.get_node_id(db,session_no_string)

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



            non_technical_question = ConnectionToNeo4j.cvQuestionGen(db,random_que)
            q_list.remove(random_que)
            print(q_list)
            print(non_technical_question)
            actual_question = QuestionCreator.gen_Question(non_technical_question)
            parser = GingerIt()
            grammer_corrected_question_list = parser.parse(actual_question)
            grammer_corrected_question = grammer_corrected_question_list.get("result")
            TextToSpeechConverter.text_to_speech(grammer_corrected_question, lang)

            if random_que=="5":
                pro = ConnectionToNeo4j.getProjects("CV", "5")
                print(pro)
                for id in range (1,pro+1):
                    pro_list.append(str(id))
                print(pro_list)


                random_proj_que = random.choice(pro_list)
                modify_random_proj_que = "p"+random_proj_que
                print(modify_random_proj_que)

                project_question = ConnectionToNeo4j.cvQuestionProjectGen(db,modify_random_proj_que,userid)
                actual_project_question = QuestionCreator.gen_Question(project_question)
                parser = GingerIt()
                grammer_corrected_project_question_list = parser.parse(actual_project_question)
                grammer_corrected_pr0ject_question = grammer_corrected_project_question_list.get("result")
                TextToSpeechConverter.text_to_speech(grammer_corrected_pr0ject_question, lang)

                global technology_list
                tech = input()

                technology_list = NestedQuestionCreator.nonTechnicalKeywordSeelector(tech,modify_random_proj_que)
                print("hello tech")
                print(technology_list)
                print("check validity")

            print("after a while")
            answer_validity = test.test()

            while(answer_validity=="None" ):
                answer_validity = test.test()



        q_list = []
        count = count+1



#
# node_Count = ConnectionToNeo4j.getNodeCount(db)
#
# process_content()
# print((word, tag)for word, tag in sentence if tag in ('NN', 'JJ'))



