import sys


sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
import heapq

h = []

for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    if n:
        heapq.heappush(h, -n)
    else:
        if not len(h):
            print(0)
        else:
            print(-heapq.heappop(h))