import sys

sys.stdin = open('input.txt')

N = int(input())

def brute(i):
    global N

    res = 0
    res += i
    n = i
    while n:
        a, b = divmod(n, 10)
        res += b
        n = a
    if res == N:
        return i
    else:
        return 0

for i in range(N):
    ans = brute(i)
    if ans:
        print(ans)
        break
else:
    print(0)
    