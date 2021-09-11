# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:00:22 2020

@author: stavy
"""

# read a string with alpha numeric characters and sum all the numbers in the string
    a += int(j)
# example:  = 100
#  hint: isnumeric() on each character will tell u if it is a number
word  = input('enter an alphanumeric')
num = ''
answer = []
for i in word:
    if i.isnumeric():
        num = num + i
    elif num != '':
#        answer.append(num)
        num=''
        print(answer)


a = 0
for j in answer:
print(a)