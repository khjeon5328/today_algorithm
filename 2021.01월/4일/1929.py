import sys


sys.stdin = open('input.txt')

# M, N = map(int, input().split())
M, N = 3, 16

estos = [False, False] + [True] * (N-1)
primes = []

for i in range(2, N+1):
    if estos[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            estos[j] = False

for i in primes:
    print(i)
