import sys


sys.stdin = open('input.txt')

N = int(input())

nums = list(map(int, input().split()))
dp = [[i, 0] for i in nums]
# print(dp)
for i in range(N):
    dp[i][1] = 1
    maxV = 1
    for j in range(i):
        if dp[i][0] > dp[j][0]:
            if maxV < dp[j][1] + 1:
                maxV = dp[j][1] + 1
    dp[i][1] = maxV
ans = 0
for i in dp:
    if i[1] > ans:
        ans = i[1]
print(ans)