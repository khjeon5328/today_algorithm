import sys


sys.stdin = open('input.txt')

N = 123456 * 2
estos = [False, False] + [True] * (N-1)
primes = []

for i in range(2, N+1):
    if estos[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            estos[j] = False
            
while True:
    n = int(input())
    if not n:
        break
    else:
        cnt = 0
        for i in primes:
            if i > n and i <= 2*n:
                cnt += 1
            elif i > 2*n:
                break
        print(cnt)