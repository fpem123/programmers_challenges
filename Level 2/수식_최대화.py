import re
from itertools import permutations

ans = 0

def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

    
def tree(expression, calc, remain):
    stack = []
    sig = False
    
    for i in range(len(expression)):
        
        if expression[i] == calc:
            stack.append(calculator(stack.pop(), expression[i + 1], calc))
            sig = True
        elif sig:
            sig = False
        else:
            stack.append(expression[i])
            
    if len(stack) == 1:
        global ans
        
        if ans < abs(stack[0]):
            ans = abs(stack[0])
        return
    
    for c in remain:
        tree(stack, c, remain - {c})
    
            
def solution(expression):
    
    nums = []
    
    p = re.compile('\D|\d+')
    q = re.compile('\D')
    
    calcs = set(q.findall(expression))
    expression = p.findall(expression)
    
    for i in range(len(expression)):
        if expression[i].isdecimal():
            expression[i] = int(expression[i])
    
    for calc in calcs:
        tree(expression, calc, calcs - {calc})
    
    return ans