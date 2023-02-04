import sys


sys.stdin = open('input.txt')


n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

ans = []
for i in range(n):
    tmp = 1
    for j in range(n):
        if i is not j:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                tmp += 1
    ans.append(tmp)
print(*ans)