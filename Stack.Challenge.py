#Challenge

#Develop a Funtion that determine whether a pice of text has matching parentheses.

# My Solution :

#count how many ( and how many )

def mached_parenthesis(text):
    if len(text) < 1:
        return None 
    else:
        count_open = 0
        count_close = 0
        for char in text:
            if char == "(":
                count_open += 1
            if char == ")":
                count_close += 1
    print("Opend = ", count_open )        
    print("Close = " , count_close)

print(mached_parenthesis("(22)"))

#Using stack

from collections import deque

stack = deque()

def check_matching_parentheses(text):
    stack = deque()
    if len(text) < 1:
        return None
    elif len(text) > 1:
        for char in text:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if len(stack) == 0:
                    return False
                stack.pop()
    return len(stack) == 0 

print(check_matching_parentheses("())"))

#version 2 whit if not stack : cheack if the stack is empty
def check_matching_parenthesesV2(text):
    stack = deque()
    if len(text) < 1:
        return None
    elif len(text) > 1:
        for char in text:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if not stack:
                    return False
                stack.pop()
    return len(stack) == 0 

print(check_matching_parenthesesV2("())"))