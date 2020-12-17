import sys


sys.stdin = open('input.txt')

# N = int(input())
N = 10000
def d(n):
    global visited
    res = 0
    res += n
    while n:
        a, b = divmod(n, 10)
        res += b
        n = a

    return res

visited = [0] * (N+1)
for i in range(1, N+1):
    res = d(i)
    if res < 10001:
        visited[res] = 1

for i in range(1, N+1):
    if not visited[i]:
        print(i)
