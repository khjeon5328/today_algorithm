import sys


sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    n = int(input())
    if n > 5:
        for i in range(5, n):
            dp[i+1] = dp[i] + dp[i-4]
    print(dp[n])
