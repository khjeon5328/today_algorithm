import sys


sys.stdin = open('input.txt')
input = sys.stdin.readline

a, b, c = map(int, input().split())

margin = c-b
if margin <= 0:
    print('-1')
else:
    print(int(a/margin)+1)