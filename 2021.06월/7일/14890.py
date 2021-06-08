import sys
from pprint import pprint
sys.stdin = open('input.txt')

input = sys.stdin.readline

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for x in range(N):
    tmp = []
    for y in range(N):
        tmp.append(arr[y][x])
    arr.append(tmp)

ans = 0
for i in range(2*N):
    visited = [-1] * N
    visited[0] = 1
    for j in range(1, N):
        if arr[i][j] == arr[i][j-1]:
            visited[j] = visited[j-1] + 1
        elif arr[i][j] - arr[i][j-1] == 1:
            if visited[j-1] >= L:
                visited[j] = 1
            else:
                break
        elif arr[i][j-1] - arr[i][j] == 1:
            if visited[j-1] >= 0:
                visited[j] = 1 - L
            else:
                break
        else:
            break
    if visited[-1] >= 0:
        # print(arr[i])
        ans += 1

print(ans)

