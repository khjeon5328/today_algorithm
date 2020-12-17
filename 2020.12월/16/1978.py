import sys

sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))
cnt = 0
def prime(n):
    global cnt
    if n > 1:
        for i in range(2, n):
            if not n%i:
                return
        cnt += 1
for i in nums:
    prime(i)
print(cnt)
