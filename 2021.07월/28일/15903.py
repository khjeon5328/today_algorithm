import sys
# from queue import PriorityQueue
import heapq

sys.stdin = open('input.txt')

N, M = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)
for _ in range(M):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    c = a+b
    heapq.heappush(cards, c)
    heapq.heappush(cards, c)

print(sum(cards))