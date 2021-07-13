import sys


sys.stdin = open('input.txt')

N = int(input())
lst = list(input())
# print(lst)
a = lst.count('A')
b = lst.count('B')
if a > b:print('A')
elif a < b: print('B')
else: print('Tie')