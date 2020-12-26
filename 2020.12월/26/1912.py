import sys

sys.stdin = open('input.txt')


N = int(input())
nums = list(map(int, input().split()))
maxV = 0
ev = [0] * N
ev[0] = nums[0]
for i in range(1, N):
    ev[i] = ev[i-1] + nums[i]
    if ev[i] < nums[i]:
        ev[i] = nums[i]
print(max(ev))