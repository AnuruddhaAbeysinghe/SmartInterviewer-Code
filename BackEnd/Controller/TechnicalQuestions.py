from BackEnd.Controller import  NonTechnicalQuestions,ConnectionToNeo4j,technicalQuestionCreator,TextToSpeechConverter,NestedQuestionCreator
import requests,math,random
from gingerit.gingerit import GingerIt

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
table_name =""


def question_gen():
    q_list = []
    lang = 'en'
    tech_keywords = NonTechnicalQuestions.technology_list
    print(tech_keywords)
    print("hey")
    nested_question_ccount = 2
    diff_level = "low"
    # strus = "java,python"

    splitted_table_list = (tech_keywords.split(',', ))
    print(splitted_table_list)
    print("list is printed")
    splitted_table_list_length = len(splitted_table_list)
    stable_splitted_table_list_length = len(splitted_table_list)
    print("length")
    print(splitted_table_list_length)
    # random_table = random.choice(splitted_table_list)
    # print(random_table)
    while splitted_table_list_length>=1:


        random_table = random.choice(splitted_table_list)
        print(random_table)
        splitted_table_list_length = splitted_table_list_length-1
        print("length")
        print(splitted_table_list_length)
        splitted_table_list.remove(random_table)
        print(splitted_table_list)

        split_list_length = stable_splitted_table_list_length
        itteration_val= int(11 / split_list_length)
        itteration_value = math.ceil(itteration_val)

        # get the nested value count after filling technologies
        rem_nested_count = 11-(split_list_length * itteration_value)
        nested_question_ccount = nested_question_ccount + rem_nested_count

        print("itt")
        print(itteration_value)


        technical_node_count = ConnectionToNeo4j.getTechNodeCount(random_table)
        print(technical_node_count)
        q_list = []
        for id in range(1, technical_node_count + 1):
            q_list.append(id)
        print(q_list)

        for itt in range(itteration_value):
            print("my itteration")
            print(itt)

            random_que = random.choice(q_list)
            print(random_que)
            random_que_string = str(random_que)
            print(random_que_string)
            technical_question = ConnectionToNeo4j.technical_question_keyword(random_table,random_que_string)
            print("qu")
            print(technical_question)
            q_list.remove(random_que)
            print(q_list)
            actual_question = technicalQuestionCreator.gen_Question(technical_question)
            parser = GingerIt()
            grammer_corrected_question_list = parser.parse(actual_question)
            grammer_cprrected_question = grammer_corrected_question_list.get("result")
            TextToSpeechConverter.text_to_speech(actual_question,lang)
            print(grammer_cprrected_question)

            if itteration_value>1 and nested_question_ccount>0:
                nested = NestedQuestionCreator.keywordSelector(random_table)
                if nested != 0:
                    print("nested keyword value")
                    actual_question = technicalQuestionCreator.gen_Question(nested)
                    TextToSpeechConverter.text_to_speech(actual_question, lang)
                    print(actual_question)

                    nested_question_ccount = nested_question_ccount - 1
                    print(nested)
                else:
                    print("when ignores")
                print("true")

            else:
                print("false")











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