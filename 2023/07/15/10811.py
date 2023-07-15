import sys
import copy

sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]




for _ in range(m):
    a, b = map(int, input().split())

    tmp = copy.deepcopy(arr[a-1:b])
    tmp.reverse()

    cnt = 0
    for i in range(a-1, b):
        arr[i] = tmp[cnt]
        cnt += 1
    tmp.clear()
print(*arr)
