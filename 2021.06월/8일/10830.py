import sys
from copy import deepcopy

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, B = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
tmp = deepcopy(A)

def dfs(n, arr):
    if n == B:
        for y in range(N):
            for x in range(N):
                A[y][x] %= 1000
            print(*A[y])
        return
    elif n == 1:
        tmp2 = deepcopy(arr)
        for y in range(N):
            for x in range(N):
                mul = 0
                for i in range(N):
                    mul += (tmp2[y][i] * tmp[i][x])
                arr[y][x] = mul
        dfs(n+1, arr)
    elif (n**2) <= B:
        tmp2 = deepcopy(arr)
        tmp3 = deepcopy(arr)
        for y in range(N):
            for x in range(N):
                mul = 0
                for i in range(N):
                    mul += (tmp2[y][i] * tmp3[i][x])
                arr[y][x] = mul
        dfs(n**2, arr)
    else:
        tmp2 = deepcopy(arr)
        for y in range(N):
            for x in range(N):
                mul = 0
                for i in range(N):
                    mul += (tmp2[y][i] * tmp[i][x])
                arr[y][x] = mul
        dfs(n+1, arr)

dfs(1, A)