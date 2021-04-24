import sys


sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
nums2 = list(map(int, input().split()))

for i in nums2:
    if i in nums:
        print(1)
    else:
        print(0)