import sys

sys.stdin = open('input.txt')

N = int(input())
nums = [0] * 10000
dp = [0] * 10000
for i in range(N):
    nums[i] = int(input())
dp[0] = nums[0]
dp[1] = dp[0] + nums[1]
dp[2] = max(nums[2] + nums[0], nums[1] + nums[2], nums[0]+ nums[1])
if N>=3:
    for i in range(3, N):
        # 해당 포도주 마시는경우
        #  1. 이전 포도주 마시는 경우
        #  2. 이전 포도주 마시지 않는 경우
        # 3. 해당 포도주 마시지 않는 경우
        dp[i] = max(nums[i] + dp[i-2], nums[i] + nums[i-1] + dp[i-3], dp[i-1])
print(max(dp))