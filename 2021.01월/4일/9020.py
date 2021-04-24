import sys

sys.stdin = open('input.txt')


size = 10000
estos = [False, False] + [True] * (size-1)
primes = []
for i in range(2, size+1):
    if estos[i]:
        primes.append(i)
        for j in range(2*i, size+1, i):
            estos[j] = False

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    minV = 0
    maxV = N
    for i in primes:
        if i <= N:
            diff = N - i
            for j in primes:
                if j >= i and diff == j:
                    minV = i
                    maxV = j
                elif j > diff:
                    break
        else:
            break
    print(minV, maxV)
