import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)