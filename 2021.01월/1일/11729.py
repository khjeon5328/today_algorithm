import sys

sys.stdin = open('input.txt')

N = int(input())


def hanoi(n, frm, to, oth):
    if n == 1:
        print(frm, to)
        return
    else:
        hanoi(n-1, frm, oth, to)
        print(frm, to)
        hanoi(n-1, oth, to, frm)

print(2**N-1)
hanoi(N, 1, 3, 2)