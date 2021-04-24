import sys


sys.stdin = open('input.txt')

A, B, C = map(int, input().split())

check = [[0] * 201 for _ in range(201)]
ans = [0] * 201

from collections import deque

def bfs():
    q = deque([(0, 0, C)])

    while q:
        x, y, z = q.popleft()
        # print(x, y, z)
        if check[x][y]:
            continue

        check[x][y] = 1

        if not x:
            ans[z] = 1
        # A --> B
        if x + y > B:
            q.append((x+y-B, B, z))
        else:
            q.append((0, x+y, z))
        # A --> C
        if x + z > C:
            q.append((x+z-C, y, C))
        else:
            q.append((0, y, x+z))

        # B --> C
        if y + z > C:
            q.append((x, y+z-C, C))
        else:
            q.append((x, 0, y+z))

        # B --> A
        if y + x > A:
            q.append((A, y+x-A, z))
        else:
            q.append((y+x, 0, z))

        # C --> A
        if z + x > A:
            q.append((A, y, x+z-A))
        else:
            q.append((x+z, y, 0))
        # C --> B
        if z + y > B:
            q.append((x, B, y+z-B))
        else:
            q.append((x, z+y, 0))
bfs()

for i in range(201):
    if ans[i]:
        print(i, end=" ")