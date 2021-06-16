import sys

sys.stdin = open('input.txt')

nums = [1, 2, 3]
def comb(n, hap):
    global ans
    if hap > n:
        return
    if hap == n:
        ans += 1
    for i in nums:
        comb(n, hap + i)


T = int(input())
for _ in range(T):
    ans = 0
    n = int(input())
    comb(n, 0)
    print(ans)
