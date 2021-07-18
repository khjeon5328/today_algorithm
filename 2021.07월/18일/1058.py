import sys


sys.stdin = open('input.txt')

N = int(input())


arr = [list(input()) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if j != k:
                if arr[j][k] == 'Y' or (arr[i][j] =='Y' and arr[i][k] =='Y'):
                    visit[j][k] = 1

ans = 0
for i in range(N):
    ans = max(ans, sum(visit[i]))
print(ans)