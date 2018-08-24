import ConnectionToNeo4j
filtered_words_string = "pickling  is  a good python concept"
filtered_words = filtered_words_string.split(" ")
db ="python"
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
print(topic_list)



# for()