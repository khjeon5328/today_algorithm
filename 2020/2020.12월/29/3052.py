import sys

sys.stdin = open('input.txt')

nums = {}
for _ in range(10):
    n = int(input())
    r = n % 42
    if r in nums:
        continue
    else:
        nums[r] = 1
print(len(nums))