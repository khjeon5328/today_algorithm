import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline
import math
N = int(input())
nums = list(map(int, input().split()))
B, C = map(int, input().split())
# print(nums)
# print(math.ceil(4.1))
ans = N
for i in range(N):
    nums[i] -= B
    if nums[i] > 0:
        ans = ans + math.ceil(nums[i] / C)
print(ans)