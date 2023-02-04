import sys

sys.stdin = open('input.txt')


def prime(n):
    if n > 1:
        for i in range(2, n):
            if not n%i:
                return 
        return n

M = int(input())
N = int(input())
nums = []
for i in range(M, N+1):
    if prime(i):
        nums.append(i)

if nums:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)