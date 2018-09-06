from BackEnd.Controller import ConnectionToNeo4j
import random

# db = "python"
def keywordSelector(db):
    filtered_words_string = " is unpickling a  good python concept overriding"
    filtered_words = filtered_words_string.split(" ")

    topic_list = []

    # print(filtered_words)
    unique_filtered_words = set()
    for val in filtered_words:
        lower_case_val = val.lower()
        unique_filtered_words.add(lower_case_val)
    # print(unique_filtered_words)

    for value in unique_filtered_words:
        topic_availability = ConnectionToNeo4j.getMatchingTopics(db,value)
        print(topic_availability)
        if topic_availability == True:
            topic_list.append(value)
    # print(topic_list)

    if len(topic_list) > 0:
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
    for value in unique_filtered_word_nontech:
        db_availability = ConnectionToNeo4j.getMatchingTopicsNonTech(value)
        if db_availability == True:
            db_list.append(value)
    if len(db_list) > 0:
        db_string_list = ','.join(db_list)
        print(db_string_list)
        return  db_string_list
    else:
        db = "CV"
        project_tech_list = ConnectionToNeo4j.cvProjectTech(db,project)
        return project_tech_list






