import sys

sys.stdin = open('input.txt')


v = 1
for _ in range(3):
    n = int(input())
    v *= n
nums = {}
for i in range(10):
    nums[f'{i}'] = 0
for i in str(v):
    if i in nums:
        nums[i] += 1
for k in nums.values():
    print(k)