import sys
import heapq


sys.stdin = open('input.txt')

tc = int(input())

for _ in range(tc):
    K = int(input())
    doc = list(map(int, input().split()))
    # print(doc)
    heapq.heapify(doc)

    cost = 0
    while len(doc) > 1:
        x1 = heapq.heappop(doc)
        x2 = heapq.heappop(doc)
        tmp = x1 + x2
        cost += tmp
        heapq.heappush(doc, tmp)
        # print(len(doc))
        print(cost, doc)
    print(cost)