import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
consult = []
dp = []
for _ in range(N):
    T, P = map(int, input().split())
    consult.append((T, P))
    dp.append(P)
dp.append(0)
for i in range(N-1, -1, -1):
    if i + consult[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], consult[i][1] + dp[i + consult[i][0]])
print(dp[0])