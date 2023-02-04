import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline
import copy

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))
tmp = copy.deepcopy(arr)

while True:
    minV = 101
    minI = []
    maxV = 0
    maxI = []
    for i in range(N):
        if arr[i] > maxV:
            maxI = []
            maxI.append(i)
            maxV = arr[i]
        elif arr[i] == maxV:
            maxI.append(i)

        if arr[i] < minV:
            minI = []
            minI.append(i)
            minV = arr[i]
        elif arr[i] == minV:
            minI.append(i)

    if maxV - minV > 17:
        if len(maxI) > len(minI):
            for i in minI:
                arr[i] += 1
        else:
            for i in maxI:
                arr[i] -= 1
    else:
        break

ans = 0
for i in range(N):
    if tmp[i] != arr[i]:
        ans += (tmp[i] - arr[i])**2
print(tmp)
print(arr)
print(ans)
