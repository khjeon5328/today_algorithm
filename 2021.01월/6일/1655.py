import sys


sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
import heapq

def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heap_sort(iter):
    n = len(iter)
    for i in range(n//2-1, -1, -1 ):
        heapify(iter, i, n)
    for i in range(n-1, 0, -1):
        iter[0], iter[i] = iter[i], iter[0]
        heapify(iter, 0, i)
    return iter
h = []
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    heapq.heappush(h, n)
    ans = heap_sort(h)
    print(ans[len(ans) // 2 - 1])
