import sys


sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
import heapq

max_h = []
min_h = []

for _ in range(N):
    n = int(sys.stdin.readline().rstrip())

    if len(max_h) == len(min_h):
        heapq.heappush(max_h, (-n, n))
    else:
        heapq.heappush(min_h, (n, n))

    if min_h and max_h[0][1] > min_h[0][1]:
        maxV = heapq.heappop(max_h)[1]
        minV = heapq.heappop(min_h)[1]

        heapq.heappush(max_h, (-minV, minV))
        heapq.heappush(min_h, (maxV, maxV))

    print(max_h[0][1])
    # print(max_h)
    # print(min_h)