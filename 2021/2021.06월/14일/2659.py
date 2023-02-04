import sys

sys.stdin = open('input.txt')

lst = list(map(int, input().split()))


def clockNum(lst):
    minV = 9999
    for i in range(4):
        tmp = ''
        for j in range(4):
            tmp += str(lst[(i+j) % 4])
        minV = min(minV, int(tmp))
    return minV
rst = clockNum(lst)

visited = [0] * 10000
for i in range(1111, rst):
    i = str(i)
    tmp = []
    for s in i:
        tmp.append(int(s))
    tmp = clockNum(tmp)
    visited[tmp] = 1

ans = 1
for i in range(1111, rst):
    if visited[i]:
        ans += 1
print(ans)