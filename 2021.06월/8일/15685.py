import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

arr = [[0 * 101] for _ in range(101)]

N = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def dragon(x, y, d, g):
    arr[y][x] = 1

for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon(x, y, d, g)