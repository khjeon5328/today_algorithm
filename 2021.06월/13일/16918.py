import sys
from collections import deque
from pprint import pprint

sys.stdin = open('input.txt')

# input = sys.stdin.readline


R, C, N = map(int, input().split())

arr = [list(input()) for _ in range(R)]


def explode():
    while bomb:
        y, x = bomb.popleft()
        arr[y][x] = '.'
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < R and 0 <= nx < C:
                arr[ny][nx] = '.'
def findBomb():
    for y in range(R):
        for x in range(C):
            if arr[y][x] == 'O':
                bomb.append((y, x))

def installBomb():
    for y in range(R):
        for x in range(C):
            arr[y][x] = 'O'


def printStatus():
    for y in range(R):
        print("".join(arr[y]))


bomb = deque()

N -= 1
time = 0

while time < N:
    if time % 2:
        explode()
    else:
        findBomb()
        installBomb()
    time += 1
printStatus()
