import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline
N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

minV = sys.maxsize
mm = min(arr)
for i in arr:
    if i == mm:
        continue
    else:
        minV = min(i, minV)
ans = []
for i in range(2, minV):
    r = arr[0] % i
    for j in range(1, N):
        if r != (arr[j] % i):
            break
    else:
        ans.append(i)
print(*ans)
    

    