import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

nums = list(map(int, input().split()))
nums.sort()
print(nums[1])