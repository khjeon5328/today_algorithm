import sys

sys.stdin = open('input.txt')

while True:
    n1, n2 = map(int, input().split())
    if n1 == n2 == 0:
        break
    if n1 > n2:
        if n1 % n2:
            print('neither')
        else:
            print('multiple')
    else:
        if n2 % n1:
            print('neither')
        else:
            print('factor')