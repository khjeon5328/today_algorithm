import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


syn = list(input())
i = int(input())
print(syn[i-1])