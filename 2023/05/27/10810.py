import sys

sys.stdin = open('input.txt')


input = sys.stdin.readline


n, m = map(int, input().split())

arr = [0 for _ in range(n)]
# print(arr)
for i in range(m):
    i, j, k = map(int, input().split())
    # print(i, j, k)

    for x in range(i-1, j):
        arr[x] = k
print(*arr)