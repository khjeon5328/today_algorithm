import sys
from pprint import pprint
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = arr[0][0]
# pprint(arr)
# pprint(dp)
for i in range(1, N):
    for j in range(1, i):
        dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    dp[i][0] = arr[i][0] + dp[i-1][0]
    dp[i][i] = arr[i][i] + dp[i-1][i-1]
# pprint(dp)
print(max(dp[N-1]))