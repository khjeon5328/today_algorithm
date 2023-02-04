import sys


sys.stdin = open('input.txt')

N, M = map(int, input().split())
trees = list(map(int, input().split()))

low = 1
high = max(trees)

while low <= high:
    mid = (low + high) // 2

    tree = 0
    for i in trees:
        if i - mid > 0:
            tree += (i - mid)
    if tree < M:
        high = mid - 1
    else:
        low = mid + 1
print(high)