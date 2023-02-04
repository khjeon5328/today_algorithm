import sys


sys.stdin = open('input.txt')
N = int(input())
maze = list(input())
print(maze)
w = 1
h = 1
arr = [[0]*w for _ in range(h)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
d = 0
