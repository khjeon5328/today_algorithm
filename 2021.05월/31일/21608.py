import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
desk = [[0] * N for _ in range(N)]


def cond1(s):
    student = s[0]
    likes = s[1:]
    maxV = 0
    max_null = 0
    loc = []
    for y in range(N):
        for x in range(N):
            if not desk[y][x]:
                cnt = 0
                null_space = 0
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0<= nx < N and 0 <= ny < N:
                        if desk[ny][nx] in likes:
                            cnt += 1
                        elif not desk[ny][nx]:
                            null_space += 1
                if cnt > maxV:
                    loc = []
                    loc.append((y, x, null_space))
                    maxV = cnt
                    max_null = null_space
                elif cnt == maxV:
                    loc.append((y, x, null_space))
                    max_null = max(max_null, null_space)
    if len(loc) > 1:
        new_loc = []
        for i in range(len(loc)):
            if loc[i][2] == max_null:
                new_loc.append((loc[i][0], loc[i][1]))
        # print(new_loc)
        if len(new_loc) > 1:
            new_loc.sort()
        desk[new_loc[0][0]][new_loc[0][1]] = student
    else:
        desk[loc[0][0]][loc[0][1]] = student



           
relation = [[]] * (N**2 + 1)
for i in range(N**2):
    s = list(map(int, input().split()))
    relation[s[0]] = (s[1:])
    cond1(s)

ans = 0
for y in range(N):
    for x in range(N):
        s = desk[y][x]
        cnt = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0<= nx < N and 0 <= ny < N and desk[ny][nx] in relation[s]:
                cnt += 1
        if cnt == 4:
            ans += 1000
        elif cnt == 3:
            ans += 100
        elif cnt == 2:
            ans += 10
        elif cnt == 1:
            ans += 1
print(ans)
