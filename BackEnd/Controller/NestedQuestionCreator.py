from BackEnd.Controller import ConnectionToNeo4j
import random

# db = "python"
def keywordSelector(db,filtered_words_string,param):

    filtered_words = filtered_words_string.split(" ")
    print(filtered_words)
    print("filtered_words")


    global  topic_list
    topic_list = []

    # print(filtered_words)
    unique_filtered_words = set()
    for val in filtered_words:
        lower_case_val = val.lower()
        unique_filtered_words.add(lower_case_val)
    print(unique_filtered_words)
    print("unique_filtered_words")

    for value in unique_filtered_words:
        if param == "2":
            topic_availability = ConnectionToNeo4j.getMatchingTopics(db,value)
            print(topic_availability)
            if topic_availability == True:
                topic_list.append(value)
        elif param == "1":
            topic_availability = ConnectionToNeo4j.getMatchingTopicsNonTech(value)
            print(topic_availability)
            if topic_availability == True:
                topic_list.append(value)
                print()
    # print(topic_list)
    if param == "1":
        topic_list = ",".join(topic_list)
        return topic_list


    if len(topic_list) > 0 and param=="2":
        random_keyword = random.choice(topic_list)
        return  random_keyword
    else:
        return 0

# keyword = keywordSelector();
# for()

def nonTechnicalKeywordSeelector(names,project):
    name_list = names.split(',')
    print("name list")
    print(name_list)
    db_list = []

    unique_filtered_word_nontech = set()
    for val in name_list:
        lower_case_value = val.lower()
        unique_filtered_word_nontech.add(lower_case_value)
        print(unique_filtered_word_nontech)
        print("error in yesterday")
    for value in unique_filtered_word_nontech:
        db_availability = ConnectionToNeo4j.getMatchingTopicsNonTech(value)
        print("error in now")
        if db_availability == True:
            db_list.append(value)
        print(db_list)
        print("it is printed")
    if len(db_list) > 0:
        db_string_list = ','.join(db_list)
        print(db_string_list)
        print("error in that")
        return  db_string_list
    else:
        db = "CV"
        project_tech_list = ConnectionToNeo4j.cvProjectTech(db,project)
        print("error in this")
        return project_tech_list







