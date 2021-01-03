import sys

sys.stdin = open('input.txt')
N = int(input())
nums = list(map(int, input().split()))
dp = [[1, 1] for _ in range(N)]
# print(nums)
# print(dp)
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j] and dp[i][0] < dp[j][0] + 1: 
            dp[i][0] = dp[j][0] + 1 

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if nums[i] > nums[j] and dp[i][1] < dp[j][1] + 1:
            dp[i][1] = dp[j][1] + 1
ans = 0
for i in dp:
    if sum(i) > ans:
        ans = sum(i)
print(ans-1)        
