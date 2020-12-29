import sys


sys.stdin = open('input.txt')

s = input()
d = {}
for i in range(97, 123):
    d[chr(i)] = -1
for i in range(len(s)):
    if d[s[i]] == -1:
        d[s[i]] = i
for v in d.values():
    print(v, end=' ')