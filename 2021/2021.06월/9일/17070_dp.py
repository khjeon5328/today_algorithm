import sys
from pprint import pprint
from collections import deque

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * N for _ in range(N)] for _ in range(3)]
#가로 세로 대각선
# pprint(dp)
# print(len(dp))
for i in range(2, N):
    if not arr[0][i]:
        dp[0][0][i-1] = 1
    else:
        break

for i in range(1, N):
    for j in range(2, N):
        #대각선
        if arr[i][j] == arr[i-1][j] == arr[i][j-1] == 0:
            dp[2][i][j] =  dp[2][i-1][j-1] + dp[0][i-1][j-1] + dp[1][i-1][j-1]
        #가로
        if arr[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])
