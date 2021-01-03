import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
nums = [0] * 10000
for _ in range(N):
    n = int(sys.stdin.readline())
    nums[n-1] += 1
for i in range(len(nums)):
    if nums[i]:
        sys.stdout.write((str(i+1) +'\n')*nums[i])

