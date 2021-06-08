import sys
from pprint import pprint

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [[0] * (N) for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1
    ladder[a-1][b] = 2

# pprint(ladder)
INF = 987654321
ans = INF

def check():
    for i in range(N):
        row = 0
        col = i
        while row < H:
            if ladder[row][col] == 1:
                col += 1
            elif ladder[row][col] == 2:
                col -= 1
            row += 1
        if i != col:
            return False
    return True


def solve(pos, cnt):
    global ans, INF

    if cnt == 3 or pos >= (N * H):
        if check():
            return cnt
        return INF

    row = pos // N
    col = pos % N

    if col + 1 < N and ladder[row][col] == 0 and ladder[row][col+1] == 0:
        ladder[row][col] = 1
        ladder[row][col+1] = 2
        ans = min(ans, solve(pos + 2, cnt + 1))
        ladder[row][col] = ladder[row][col+1] = 0 

    ans = min(ans, solve(pos + 1, cnt))
    return ans

a = solve(0, 0)
if a == INF:
    print(-1)
else:
    print(a)