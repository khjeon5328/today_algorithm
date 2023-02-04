import sys


sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

minV = sys.maxsize
def comb(n, visited, s):
    global minV
    if n == N:
        minV = min(s, minV)
        return

    if s >= minV:
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            comb(n+1, visited, s + A[i] * B[n])
            visited[i] = 0

comb(0, [0]*N, 0)

print(minV)