import sys
from pprint import pprint 

sys.stdin = open('input.txt')


input = sys.stdin.readline


n = int(input())

wall = [[0 for _ in range(100)] for _ in range(100)]
# print(wall[99][99])

for i in range(n):
    x, y = map(int, input().split())
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            if i < 100 and j < 100 and not wall[i][j]:
                wall[i][j] = 1

ans = 0
for i in range(len(wall)):
    ans += sum(wall[i])
print(ans)