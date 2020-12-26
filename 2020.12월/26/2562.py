import sys

sys.stdin = open('input.txt')

nums = []
for _ in range(9):
    nums.append(int(input()))

maxV = max(nums)
print(maxV)
print(nums.index(maxV) + 1)