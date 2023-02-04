#실패 다시풀기

import sys
from pprint import pprint


sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
arr = [[0] * (N + 1)]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))


# pprint(arr)

# 1.d1, d2 ≥ 1
# 2. 0 ≤ x < x+d1+d2 < N
# 3. 0 ≤ y-d1 < y < y+d2 < N

# (x, y), (x+1, y-1), ..., (x+d1, y-d1)
# (x, y), (x+1, y+1), ..., (x+d2, y+d2)
# (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
# (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)

minV = sys.maxsize
minPop = []
def calc(y, x, d1, d2):
    global minV, minPop

    tmp = [[0] * (N+1) for _ in range(N+1)]
    population = [0 for i in range(6)]

    for i in range(d1 + 1):
        tmp[x + i][y - i] = 5
        tmp[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        tmp[x + i][y + i] = 5
        tmp[x + d1 + i][y - d1 + i] = 5

    for i in range(x + 1, x + d1 + d2):
        isTrue = False
        for j in range(1, N + 1):
            if tmp[i][j] == 5: isTrue = not isTrue
            if isTrue: tmp[i][j] = 5

   
    for r in range(1, N+1):
        for c in range(1, N+1):
            if 1 <= r < x+d1 and 1 <= c <= y and not tmp[r][c]: population[1] += arr[r][c]
            elif 1 <= r <= x+d2 and y < c <= N and not tmp[r][c]: population[2] += arr[r][c]
            elif x+d1 <= r <= N and 1 <= c < y-d1+d2 and not tmp[r][c]: population[3] += arr[r][c]
            elif x+d2 < r <= N and y-d1+d2 <= c <= N and not tmp[r][c]: population[4] += arr[r][c]
            elif tmp[r][c] == 5: population[5] += arr[r][c]
    return max(population[1:]) - min(population[1:])


    # 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    # 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    # 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    # 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N



ans = sys.maxsize
for y in range(1, N+1):
    for x in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if x + d1 + d2 <= N and 1 <= y - d1 < y < y + d2 <= N:
                    ans = min(ans, calc(y, x, d1, d2))
print(ans)