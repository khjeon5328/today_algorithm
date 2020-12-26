import sys


sys.stdin = open('input.txt')

N = int(input())

chars = []
for _ in range(N):
    i = str(input())
    if i not in chars:
        chars.append(i)
chars.sort()
ans = sorted(chars, key=len)
# print(ans)
for i in ans:
    print(i)