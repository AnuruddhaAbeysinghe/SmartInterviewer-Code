<<<<<<< HEAD
nested_question_ccount = 2
split_list_length = 3
itteration_value = 3
rem_nested_count = 11-(split_list_length * itteration_value)
nested_question_ccount = nested_question_ccount + rem_nested_count
print(rem_nested_count)
print(nested_question_ccount)
=======
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sentence2 = "give up it has a role similar to path this variable tells the Python interpreter where to locate the module files imported into a program It should include the Python source library directory and the directories containing Python source code"


stopWords = set(stopwords.words('english'))

words2 = word_tokenize(sentence2)

wordsFiltered2 = []


for w in words2:
    if w not in stopWords:
        wordsFiltered2.append(w)

final_word = ""


for word in wordsFiltered2:
    final_word = final_word+" "+word

print(final_word)







>>>>>>> fc959a6a910905690ad801b908a81b2096fb8b33