# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 21:54:23 2018

@author: ASUS
"""


import numpy as np
from xml.etree import ElementTree as ET
from BackEnd.Controller import ConnectionToNeo4j
#import matlab-python as matlab



#---------------------------------------------------------------------------------------------
#Identify the state
 
facial = int(input("Facial :"))
voice = int(input("Voice :"))
answer = int(input("Answer :"))

total = (facial + voice + answer)

print("Total = ",total)
total = int(total)

if (0 < total <= 20):
    state = 1
    print ("State = ",state)

elif (21 < total <= 40):
    state = 2
    print ("State = ",state)

elif (41 < total <= 60):
    state = 3
    print ("State = ",state)

elif (61 < total <= 80):
    state = 4
    print ("State = ",state)

else:
    state = 5
    print ("State = ",state)



#----------------------------------------------------------------------------------------------------------------
#Create the metrix

# R = np.matrix([[0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0]])

# R = np.matrix([[64.0, 64.0, 64.0, 80.0, 64.0],
#                [64.0, 64.0, 64.0, 80.0, 64.0],
#                [64.0, 64.0, 64.0, 80.0, 64.0],
#                [64.0, 100.0, 64.0, 80.0, 64.0],
#                [64.0, 64.0, 64.0, 80.0, 64.0]])

# R = np.matrix([[87.679663, 99.119352, 98.879943, 98.607253, 81.504678],
#                [77.586842, 98.634585, 99.156076, 97.516682, 99.509751],
#                [95.848135, 98.676680, 97.443117, 99.802724, 94.070595],
#                [99.338241, 88.679581, 99.776517, 99.607346, 75.542234],
#                [98.925505, 97.981062, 100.000000, 98.545958, 20.230419]])






# R = np.matrix([[96.0, 96.0, 96.0, 100.0, 96.0],
#                [96.0, 96.0, 96.0, 100.0, 96.0],
#                [96.0, 96.0, 96.0, 100.0, 96.0],
#                [96.0, 96.25, 96.0, 100.0, 96.0],
#                [96.0, 96.0, 96.0, 100.0, 96.0]])

# R = np.matrix([[99.2000, 99.2000, 99.2000, 99.2000, 99.2000],
#                [99.2000, 99.2000, 99.2000, 99.2000, 99.2000],
#                [99.2000, 99.2000, 99.2000, 99.2000, 99.2000],
#                [99.2000, 93.0000, 99.2000, 99.2000, 99.2000],
#                [99.2000, 99.2000, 99.2000, 99.2000, 99.2000]])

# R = np.matrix([[92.807644, 99.889420, 99.288169, 95.151532, 92.370516],
#                [99.712525, 100.000000, 99.288169, 85.721550, 93.808366],
#                [98.551180, 99.019491, 99.372452, 96.489693, 99.185307],
#                [96.278086, 98.261064, 93.921858, 98.795678, 93.808366],
#                [94.053272, 97.200365, 98.659636, 96.489693, 97.971093]])



# -------------------------------------------------------------------------------
# Get the latest Q-table reguarding the language

fname = "../Database/text.txt"

with open(fname, 'r') as f:
    R = np.genfromtxt(f,dtype="float")

data = R
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
# if R is None:
#     print("No value")
# else:
#     print("Testing 1")
#     print(ConnectionToNeo4j.createQtable(R))

# ConnectionToNeo4j.createQtable(R)

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

#-----------------------------------------------------------------------------------
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("Get from ontology \n",ConnectionToNeo4j.createQtable1())
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#-----------------------------------------------------------------------------------

R = np.matrix(R)

# matrix = open(fname).read()
# matrix = [item.split('\n') for item in matrix.split('\n')]
# R = matrix.reshape((matrix.shape[0], 5))


print("Get from text file-latest updated \n",R)

print("----------------------------------------------")
# Q matrix
Q = np.matrix(np.zeros([5, 5]))

if state == 1:
    R[0,4] = total
elif state == 2:
    R[1,3] = total
elif state == 3:
    R[2,2] = total
elif state == 4:
    R[3,1] = total
else:
    R[4,0] = total


# Gamma (learning parameter).
gamma = 0.8

#Initial state
if state == 5:
    initial_state = 4
else:
    initial_state = state


#initial_state = state
# This function returns all available actions in the state given as an argument
def available_actions(state):
    current_state_row = R[state,]
    av_act = np.where(current_state_row >= 0)[1]
    return av_act


# Get available actions in the current state
available_act = available_actions(initial_state)


# This function chooses at random which action to be performed within the range
def sample_next_action(available_actions_range):
    next_action = int(np.random.choice(available_act, 1))
    return next_action

# Sample next action to be performed
action = sample_next_action(available_act)


# This function updates the Q matrix
def update(current_state, action, gamma):
    max_index = np.where(Q[action,] == np.max(Q[action,]))[1]

    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]

    # Q learning formula
    Q[current_state, action] = R[current_state, action] + gamma * max_value

# Update Q matrix
update(initial_state, action, gamma)

# -------------------------------------------------------------------------------
# Create the reward value

# iterarte the process
for i in range(100):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    update(current_state, action, gamma)
print("-----------------------")
print("New updated one \n",Q)
print("-----------------------")
#----------------------------------------------------------------------------------------------------------------
#Save the Q-metrix in text file

print(" Maximum value:")
print(np.max(Q))
T = Q * 100 / np.max(Q)
np.savetxt('../Database/text.txt', T, fmt='%f')


# -------------------------------------------------------------------------------
# convert to probability value

if state == 3:
    convertProb = "{0:.0f}%".format((np.max(Q) / 10)-11)
    # convertProb = getProb - 10.0
    print("Precentage of difficulty - ",convertProb)
else:
    convertProb = "{0:.0f}%".format(np.max(Q) / 10)
    print("Precentage of difficulty - ",convertProb)



# -------------------------------------------------------------------------------
# update the XML file

tree = ET.parse('../Database/rewardValue.xml')
root = tree.getroot()

# modifying an attribute Language
for elem in root.iter('language'):
    elem .set('name', 'java')

# modifying an attribute Session
for elem in root.iter('session'):
    elem.set('name', '1')

# changing a field text
for elem in root.iter('session'):
    elem.text = convertProb

tree.write('../Database/rewardValue.xml')

