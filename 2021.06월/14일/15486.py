import sys

sys.stdin = open('input.txt')

N = int(input())


time = [0] * (N + 1)
pay = [0] * (N + 1)
dp = [0] * (N + 2)
for i in range(1, N + 1):
    T, P = map(int, input().split())
    time[i] = T
    pay[i] = P

if time[-1] == 1:
    dp[-2] = pay[-1]

for i in range(N-1, 0, -1):
    if i + time[i] <= N + 1:
        dp[i] = max(pay[i] + dp[i+time[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[1])