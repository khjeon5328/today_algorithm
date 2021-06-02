import sys
import copy

sys.stdin = open('input.txt')
input = sys.stdin.readline

#5
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

maxV = 0

def up(easy):
    for x in range(N):
        p = 0
        tmp = 0
        for y in range(N):
            if not easy[y][x]:
                continue
            if not tmp:
                tmp = easy[y][x]
            else:
                if tmp == easy[y][x]:
                    easy[p][x] = tmp * 2
                    tmp = 0
                else:
                    easy[p][x] = tmp
                    tmp = easy[y][x]
                p += 1
            easy[y][x] = 0
        if tmp:
            easy[p][x] = tmp
    return easy

def left(easy):
    for y in range(N):
        p = 0
        tmp = 0
        for x in range(N):
            if not easy[y][x]:
                continue
            if not tmp:
                tmp = easy[y][x]
            else:
                if tmp == easy[y][x]:
                    easy[y][p] = tmp * 2
                    tmp = 0
                else:
                    easy[y][p] = tmp
                    tmp = easy[y][x]
                p += 1
            easy[y][x] = 0
        if tmp:
            easy[y][p] = tmp
    return easy

def down(easy):
    for x in range(N):
        p = N-1
        tmp = 0
        for y in range(N-1, -1, -1):
            if not easy[y][x]:
                continue
            if not tmp:
                tmp = easy[y][x]
            else:
                if tmp == easy[y][x]:
                    easy[p][x] = tmp * 2
                    tmp = 0
                else:
                    easy[p][x] = tmp
                    tmp = easy[y][x]
                p -= 1
            easy[y][x] = 0
        if tmp:
            easy[p][x] = tmp
    return easy

def right(easy):
    for y in range(N):
        p = N-1
        tmp = 0 
        for x in range(N-1, -1, -1):
            if not easy[y][x]:
                continue
            if not tmp:
                tmp = easy[y][x]
            else:
                if tmp == easy[y][x]:
                    easy[y][p] = tmp * 2
                    tmp = 0
                else:
                    easy[y][p] = tmp
                    tmp = easy[y][x]
                p -= 1
            easy[y][x] = 0
        if tmp:
            easy[y][p] = tmp
    return easy

def dfs(easy, n):
    global maxV
    if n == 5:
        for i in range(N):
            maxV = max(maxV, max(easy[i]))
        return 
    dfs(up(copy.deepcopy(easy)), n+1)
    dfs(left(copy.deepcopy(easy)), n+1)
    dfs(down(copy.deepcopy(easy)), n+1)
    dfs(right(copy.deepcopy(easy)), n+1)


dfs(arr, 0)
# print(up(arr))

print(maxV)