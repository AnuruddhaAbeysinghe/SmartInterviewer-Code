# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 21:54:23 2018

@author: ASUS
"""

import numpy as np
from xml.etree import ElementTree as ET
from BackEnd.Controller import ConnectionToNeo4j
import irregular as re


# import matlab-python as matlab


# ---------------------------------------------------------------------------------------------
# Identify the state

facial = int(input("Facial :"))
voice = int(input("Voice :"))
answer = int(input("Answer :"))

total = (facial + voice + answer)

print("Total = ", total)
total = int(total)

if (0 < total <= 20):
    state = 1
    print("State = ", state)

elif (21 < total <= 40):
    state = 2
    print("State = ", state)

elif (41 < total <= 60):
    state = 3
    print("State = ", state)

elif (61 < total <= 80):
    state = 4
    print("State = ", state)

else:
    state = 5
    print("State = ", state)

# -----------------------------------------------------------------------------------
K= "python"
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("Get from ontology \n", ConnectionToNeo4j.createQtable1(K))
print(type(ConnectionToNeo4j.createQtable1(K)))
#R = ConnectionToNeo4j.createQtable1(K)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# -----------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# Get the latest Q-table reguarding the language

# fname = "../Database/text.txt"
#
# with open(fname, 'r') as f:
#     R = np.genfromtxt(f, dtype="float")

#data = R
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
# if R is None:
#     print("No value")
# else:
#     print("Testing 1")
#     print(ConnectionToNeo4j.createQtable(R))

# ConnectionToNeo4j.createQtable(R)

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#Get the String array matrix from ontology - split
I = np.array(ConnectionToNeo4j.createQtable1(K)).tolist()
Z = I.split(" ")
print(Z)
print(type(Z))

#get only numbers from the list
# number = [num for num in Z if isinstance(num, (int,float))]
# print(number)

#to remove the []
number = " ".join(Z)
print(number)
print("this remove[]")
print(type(number))

P = np.fromstring(number, dtype=float)
print(P)
# H = P.resize(5,5)
# print("this is after resize")
# print(H)
# print(type(H))
H= np.reshape(P, (0, ))
print(H)
print(type(H))

#H = [float(i) if '.' in i else int(i) for i in number]
#H = np.asfarray(number,float)
#print("This str - float")
#print(type(H))
#Re-change it into 5,5 array
#J = H.reshape(5,5)
#print(type(J))
#print(J)

#change it into matrix
R = np.matrix(number)
print(type(R))

#R = np.array(J, dtype=np.float32)
print(R)
# try:
#     I = float(ConnectionToNeo4j.createQtable1(K))
#     R = np.matrix(I)
# except ValueError:
#     print("That is not a valid number of miles")

# matrix = open(fname).read()
# matrix = [item.split('\n') for item in matrix.split('\n')]
# R = matrix.reshape((matrix.shape[0], 5))


# print("Get from text file-latest updated \n", R)

print("----------------------------------------------")
# Q matrix
Q = np.matrix(np.zeros([5, 5]))

if state == 1:
    R[0, 4] = total
elif state == 2:
    R[1, 3] = total
elif state == 3:
    R[2, 2] = total
elif state == 4:
    R[3, 1] = total
else:
    R[4, 0] = total

# Gamma (learning parameter).
gamma = 0.8

# Initial state
if state == 5:
    initial_state = 4
else:
    initial_state = state


# initial_state = state
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
print("New updated one \n", Q)
print("-----------------------")
# ----------------------------------------------------------------------------------------------------------------
# Save the Q-metrix in text file

print(" Maximum value:")
print(np.max(Q))
T = Q * 100 / np.max(Q)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(T)
np.savetxt('../Database/text.txt', T, fmt='%f')

#-------------------------------------------------------
# send to ontology

J = str(T)

ConnectionToNeo4j.sendQtable(K,J)
# -------------------------------------------------------------------------------
# convert to probability value

if state == 3:
    convertProb = "{0:.0f}%".format((np.max(Q) / 10) - 11)
    # convertProb = getProb - 10.0
    print("Precentage of difficulty - ", convertProb)
else:
    convertProb = "{0:.0f}%".format(np.max(Q) / 10)
    print("Precentage of difficulty - ", convertProb)

# -------------------------------------------------------------------------------
# update the XML file

#-----------------------
F= np.reshape(T, (0, ))
print(F)

tree = ET.parse('../Database/rewardValue.xml')
root = tree.getroot()

# modifying an attribute Language
for elem in root.iter('language'):
    elem.set('name', 'java')

# modifying an attribute Session
for elem in root.iter('session'):
    elem.set('name', '1')

# changing a field text
for elem in root.iter('session'):
    elem.text = T

tree.write('../Database/rewardValue.xml')

