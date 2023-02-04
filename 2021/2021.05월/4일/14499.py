import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M, Y, X, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dice = [0] * 6

def right(dice):
    new_dice = [0] * 6
    new_dice[0] = dice[2]
    new_dice[1] = dice[1]
    new_dice[2] = dice[5]
    new_dice[3] = dice[3]
    new_dice[4] = dice[0]
    new_dice[5] = dice[4]
    return new_dice

def down(dice):
    new_dice = [0] * 6
    new_dice[0] = dice[0]
    new_dice[1] = dice[2]
    new_dice[2] = dice[3]
    new_dice[3] = dice[4]
    new_dice[4] = dice[1]
    new_dice[5] = dice[5]
    return new_dice

def left(dice):
    new_dice = [0] * 6
    new_dice[0] = dice[4]
    new_dice[1] = dice[1]
    new_dice[2] = dice[0]
    new_dice[3] = dice[3]
    new_dice[4] = dice[5]
    new_dice[5] = dice[2]
    return new_dice

def up(dice):
    new_dice = [0] * 6
    new_dice[0] = dice[0]
    new_dice[1] = dice[4]
    new_dice[2] = dice[1]
    new_dice[3] = dice[2]
    new_dice[4] = dice[3]
    new_dice[5] = dice[5]
    return new_dice

order = list(map(int, input().split()))
for i in order:
    # print(dice)
    if i == 1:
        if 0 <= X + 1 < M:
            X += 1
            dice = right(dice)
            if arr[Y][X]:
                dice[2] = arr[Y][X]
                arr[Y][X] = 0
            else:
                arr[Y][X] = dice[2]
            print(dice[4])
    elif i == 2:
        if 0 <= X - 1 < M:
            X -= 1
            dice = left(dice)
            if arr[Y][X]:
                dice[2] = arr[Y][X]
                arr[Y][X] = 0
            else:
                arr[Y][X] = dice[2]
            print(dice[4])
    elif i == 3:
        if 0 <= Y - 1 < N:
            Y -= 1
            dice = up(dice)
            if arr[Y][X]:
                dice[2] = arr[Y][X]
                arr[Y][X] = 0
            else:
                arr[Y][X] = dice[2]
            print(dice[4])
    elif i == 4:
        if 0 <= Y + 1 < N:
            Y += 1
            dice = down(dice)
            if arr[Y][X]:
                dice[2] = arr[Y][X]
                arr[Y][X] = 0
            else:
                arr[Y][X] = dice[2]
            print(dice[4])