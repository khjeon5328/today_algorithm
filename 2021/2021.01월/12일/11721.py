import sys


sys.stdin = open('input.txt')

word = list(input())

n = len(word)
a,b = divmod(n, 10)
for i in range(a):
    print("".join(word[i*10:(i+1)*10]))
if b:
    print("".join(word[-b:]))