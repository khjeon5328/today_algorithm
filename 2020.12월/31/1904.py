import sys


N = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, N):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
# print(dp)
print(dp[N])