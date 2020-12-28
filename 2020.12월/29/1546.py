import sys

sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))
maxV = max(nums)
for i in range(N):
    nums[i] = (nums[i] / maxV) * 100

print(sum(nums)/N)