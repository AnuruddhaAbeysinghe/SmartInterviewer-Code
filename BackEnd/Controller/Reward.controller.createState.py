# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:37:25 2018

@author: Anuruddha
"""
#have to change with the created variables of emotion & answer veri.
facial = 13.0;
voice = 15.0;
answer = 35.0;

total = facial + voice + answer;

print total;

if(0<total<=20):
    state = 1
    print state
    
elif(20<total<=40):
    state = 2
    print state

elif(40<total<=60):
    state = 3
    print state

elif(60<total<=80):
    state = 4
    print state

else:
    state = 5
    print state
 
#this is to get the state out as a variable    
state2 = state + 10
print state2
