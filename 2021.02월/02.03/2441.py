import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
for i in range(n):
    print(' '*i+'*'*(n-i))
