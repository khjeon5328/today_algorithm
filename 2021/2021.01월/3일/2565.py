from pprint import pprint
import sys


sys.stdin = open('input.txt')

N = int(input())
lines = []
for _ in range(N):
    a, b = map(int, input().split())
    lines.append([a, b, 1])
lines.sort()

for i in range(N):
    maxV = 0
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            if lines[j][2] > maxV:
                maxV = lines[j][2]
    lines[i][2] += maxV
ans = 0
for i in lines:
    if i[2]> ans:
        ans = i[2]
print(N-ans)