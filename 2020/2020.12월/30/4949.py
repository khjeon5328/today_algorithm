import sys


sys.stdin = open('input.txt')
from collections import deque
while True:
    l = input()
    # print(l)
    stack = deque()
    ans = 'yes'
    if l == '.':
        break
    for i in l:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack):
                if stack[-1] == '(':
                    stack.pop()
                else:
                    ans = 'no'
                    break
            else:
                ans = 'no'
                break
        elif i == ']':
            if len(stack):
                if stack[-1] == '[':
                    stack.pop()
                else:
                    ans = 'no'
                    break
            else:
                ans = 'no'
                break
    if len(stack):
        ans = 'no'
    print(ans)
