import sys
from pprint import pprint
from collections import deque

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# pprint(arr)

ans = 0

def check1(y, x):
    x += 1
    if x < N and not arr[y][x]:
        return True
    return False

def check2(y, x):
    y += 1
    if y < N and not arr[y][x]:
        return True
    return False

def check3(y, x):
    for dx, dy in [(1, 0), (0, 1), (1, 1)]:
        ny = y + dy
        nx = x + dx
        if ny >= N or nx >= N or arr[ny][nx]:
            return False
    return True


def bfs():
    global ans
    q = deque([(0, 0, 1)])

    while q:
        # print(q)
        d, y, x = q.popleft()

        if y == N-1 and x == N-1:
            ans += 1
        else:
            if d == 0:
                if check1(y, x):
                    q.append((0, y, x+1))
                if check3(y, x):
                    q.append((2, y+1, x+1))
            elif d == 1:
                if check2(y, x):
                    q.append((1, y+1, x))
                if check3(y, x):
                    q.append((2, y+1, x+1))
            else:
                if check1(y, x):
                    q.append((0, y, x+1))
                if check2(y, x):
                    q.append((1, y+1, x))
                if check3(y, x):
                    q.append((2, y+1, x+1))
bfs()
print(ans)