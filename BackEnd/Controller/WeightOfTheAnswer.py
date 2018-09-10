import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize("it has a role similar to path this variable tells the Python interpreter where to locate the module files imported into a program It should include the Python source library directory and the directories containing Python source code")



# CC	coordinating conjunction
# CD	cardinal digit
# DT	determiner
# EX	existential there (like: "there is" ... think of it like "there exists")
# FW	foreign word
# IN	preposition/subordinating conjunction
# checksent1 = None

# JJ	adjective	'big'
# JJR	adjective, comparative	'bigger'
# JJS	adjective, superlative	'biggest'
# LS	list marker	1)
# MD	modal	could, will
# checkAdj = None
#
# NN	noun, singular 'desk'
# NNS	noun plural	'desks'
# NNP	proper noun, singular	'Harrison'
# NNPS	proper noun, plural	'Americans'
# checkNoun = None
#
# POS	possessive ending	parent\'s
# PRP	personal pronoun	I, he, she
# PRP$	possessive pronoun	my, his, hers
# checkProN = None

#PDT	predeterminer	'all the kids'
# RB	adverb	very, silently,
# RBR	adverb, comparative	better
# RBS	adverb, superlative	best
# RP	particle	give up
# checkAdverb = None
#
# VB	verb, base form	take
# VBD	verb, past tense	took
# VBG	verb, gerund/present participle	taking
# VBN	verb, past participle	taken
# VBP	verb, sing. present, non-3d	take
# VBZ	verb, 3rd person sing. present	takes
# checkVerb = None



def process_content():
    try:
        tagged = []
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

        print(tagged)

    except Exception as e:
        print(str(e))


process_content()