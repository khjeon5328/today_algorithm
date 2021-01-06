import sys
import heapq

sys.stdin = open('input.txt')


N = int(sys.stdin.readline().rstrip())

h = []
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())

    if n:
        heapq.heappush(h, (abs(n), n))
    else:
        if len(h):
            ans = heapq.heappop(h)
            print(ans[1])
        else:
            print(0)