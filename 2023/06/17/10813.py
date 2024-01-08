import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(n+1)]

# print(arr)

for i in range(m):
    a, b = map(int, input().split())
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp
print(*arr[1:])

