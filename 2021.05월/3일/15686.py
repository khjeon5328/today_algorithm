import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

from itertools import combinations

home = []
ckn = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append([i, j])
        elif arr[i][j] == 2:
            ckn.append([i, j])
comb = list(combinations(ckn, M))

def calc(lst):
    ans = 0
    for loc in home:
        minV = sys.maxsize
        for c_loc in lst:
            minV = min(minV, abs(c_loc[0] - loc[0]) + abs(c_loc[1] - loc[1]))
        ans += minV
    return ans

ans = sys.maxsize
for i in comb:
    ans = min(ans, calc(i))
print(ans)
