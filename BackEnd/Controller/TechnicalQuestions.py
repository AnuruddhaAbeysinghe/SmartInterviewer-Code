from BackEnd.Controller import  test,NonTechnicalQuestions,ConnectionToNeo4j,technicalQuestionCreator,TextToSpeechConverter,NestedQuestionCreator
from BackEnd.Controller import DifficultyLevelSelector,vari
import requests,math,random
from gingerit.gingerit import GingerIt

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
table_name =""
answer_validy = 0

def question_gen():
    #difficulty level  generation
    global changed_know_list
    changed_know_list = []

    global diff_level
    diff_level = "easy"

    session_db = "session"

    userId = vari.userId
    sessionId = vari.sessionId
    question_number = NonTechnicalQuestions.question_number



    global taking_list
    taking_list= []

    global prev1_ans_result
    prev1_ans_result= 0.2

    global prev2_ans_result
    prev2_ans_result= 0.2

    global prev1_que_count
    prev1_que_count = 6

    global prev2_que_count
    prev2_que_count = 7

    global db_diff
    db_diff = "difficulty"







    q_list = []
    lang = 'en'
    tech_keywords = NonTechnicalQuestions.technology_list
    print(tech_keywords)
    print("hey")
    global nested_question_ccount
    nested_question_ccount = 2




    splitted_table_list = (tech_keywords.split(',', ))
    print(splitted_table_list)
    print("list is printed")
    splitted_table_list_length = len(splitted_table_list)
    stable_splitted_table_list_length = len(splitted_table_list)
    print("length")
    print(splitted_table_list_length)

    split_list_length = stable_splitted_table_list_length
    itteration_val = int(11 / split_list_length)
    itteration_value = math.floor(itteration_val)

    # get the nested value count after filling technologies
    rem_nested_count = 11 - (split_list_length * itteration_value)
    nested_question_ccount = nested_question_ccount + rem_nested_count
    print(nested_question_ccount)
    print("this is theeeeeeeeeeeeeeerem_nested_count")

    print("itt")
    print(itteration_value)




    while splitted_table_list_length>=1:


        random_table = random.choice(splitted_table_list)
        print(random_table)





        splitted_table_list_length = splitted_table_list_length-1
        print("length")
        print(splitted_table_list_length)
        splitted_table_list.remove(random_table)
        print(splitted_table_list)











        technical_node_count = ConnectionToNeo4j.getTechNodeCount(random_table)
        print(technical_node_count)
        q_list = []
        for id in range(1, technical_node_count + 1):
            q_list.append(id)
        print(q_list)



        for itt in range(itteration_value):
            print(itt)
            print("my itteration")
            print(itt)

            # difficulty level  selection
            if prev1_ans_result >= 0.5 and prev2_ans_result >= 0.5:
                diff_level = DifficultyLevelSelector.increase_difficulty_level(diff_level)
            elif prev1_ans_result < 0.5 and prev2_ans_result < 0.5:
                diff_level = DifficultyLevelSelector.decrease_difficulty_level(diff_level)
            print(diff_level)

            # get the list of nodes according to the difficulty level
            taking_list = DifficultyLevelSelector.adding_diff_level_val_list(userId, db_diff, random_table, diff_level)
            print(taking_list)
            print("hi i am the taking list")

            # comparing two lists to get the nodes that are in the q_list
            changed_know_list = set(q_list) & set(taking_list)
            print("i know it is hereeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            print(changed_know_list)
            changed_know_list = list(changed_know_list)


            random_que = random.choice(changed_know_list)
            print(random_que)
            random_que_string = str(random_que)
            print(random_que_string)
            technical_question = ConnectionToNeo4j.technical_question_keyword(random_table,random_que_string)
            print("qu")
            print(technical_question)
            changed_know_list = []
            q_list.remove(random_que)
            print(q_list)
            print(changed_know_list)
            actual_question = technicalQuestionCreator.gen_Question(technical_question)
            parser = GingerIt()
            grammer_corrected_question_list = parser.parse(actual_question)
            grammer_cprrected_question = grammer_corrected_question_list.get("result")
            TextToSpeechConverter.text_to_speech(actual_question,lang)
            print(grammer_cprrected_question)
            question_number = question_number+1
            prev1_que_count = prev1_que_count+1
            prev2_que_count = prev2_que_count+1

            answer_validity = test.test()

            while (answer_validity == "null"):
                answer_validity = test.test()

            if itt>1 and nested_question_ccount>0:
                nested = NestedQuestionCreator.keywordSelector(random_table)
                if nested != 0:
                    print("nested keyword value")
                    actual_question = technicalQuestionCreator.gen_Question(nested)
                    TextToSpeechConverter.text_to_speech(actual_question, lang)
                    print(actual_question)
                    question_number = question_number +1
                    prev1_que_count = prev1_que_count + 1
                    prev2_que_count = prev2_que_count + 1

                    nested_question_ccount = nested_question_ccount - 1
                    print(nested)

                    answer_validity = test.test()

                    while (answer_validity == "null"):
                        answer_validity = test.test()
                else:
                    print("when ignores")
                print("true")

            else:
                print("false")



            qno = str(question_number)
            send_question = "q"+qno
            print(qno)
            print(prev1_que_count)
            print(prev2_que_count)

            print("nooooooooooooooooooooooooooo")
            if prev1_que_count == 7:
                prev1_ans_result = 0.2
                prev2_ans_result = ConnectionToNeo4j.getQuestionMarks(session_db,userId,sessionId,send_question)
            else:
                prev1_ans_result = ConnectionToNeo4j.getQuestionMarks(session_db,userId,sessionId,send_question)
                prev2_ans_result = ConnectionToNeo4j.getQuestionMarks(session_db,userId,sessionId,send_question)















                # techs = NonTechnicalQuestions.technology_list
    # print(techs)
    # lang = 'en'
    # q_list = []
    # for id in range(1,5):
    #     q_list.append(str(id))
    #
    # print(q_list)
    #
    # for question_no  in range(4):
    #     time.sleep(5)
    #     random_que = random.choice(q_list)
    #     technical_question=ConnectionToNeo4j.ontologyQuestionGen(random_que)
    #     q_list.remove(random_que)
    #     actual_question = "What is "+technical_question+"?"
    #     TextToSpeechConverter.text_to_speech(actual_question, lang)
    #     print(actual_question)
    #
# question_gen()