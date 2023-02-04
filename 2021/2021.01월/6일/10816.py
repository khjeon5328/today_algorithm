import sys


sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums_d = {}
for i in nums:
    if i in nums_d:
        nums_d[i] += 1
    else:
        nums_d[i] = 1

M = int(sys.stdin.readline().rstrip())
check = list(map(int, sys.stdin.readline().rstrip().split()))
for i in check:
    if i in nums_d:
        print(nums_d[i], end=' ')
    else:
        print(0, end=' ')

