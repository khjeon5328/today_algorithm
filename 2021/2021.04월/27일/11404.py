import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline
INF = sys.maxsize



N = int(input())
M = int(input())
arr = [[INF]*N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    arr[a][b] = min(c, arr[a][b])

def Floyd_Warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    arr[i][j] = 0
                elif arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == INF:
                print(0, end=" ")
            else:
                print(arr[i][j], end=" ")
        print()

Floyd_Warshall()