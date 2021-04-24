import sys


sys.stdin = open('input.txt')

# input = sys.stdin.readline

def rotation(summary):
    global gear
    for v in summary:
        n = v[0]
        d = v[1]
        if d == 1:
            r = gear[n].pop(-1)
            gear[n].insert(0, r)
        else:
            r = gear[n].pop(0)
            gear[n].append(r)


gear = [list(map(int, input())) for _ in range(4)]
T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    N -= 1

    # print(gear)
    summary = [[N, D]]
    left = N
    left_d = D
    right = N
    right_d = D

    while True:
        if left == 0:
            break

        if gear[left][6] != gear[left-1][2]:
            summary.append([left-1, -left_d])
            left -= 1
            left_d = -left_d
        else:
            break

    while True:
        if right == 3:
            break
        if gear[right][2] != gear[right+1][6]:
            summary.append([right+1, -right_d])
            right += 1
            right_d = -right_d
        else:
            break

    rotation(summary)
    # print(summary)
hap = 0
w = 1
for i in range(4):
    if gear[i][0] == 1:
        hap += w
    w *= 2
print(hap)