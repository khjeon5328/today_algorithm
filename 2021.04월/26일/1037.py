import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)

print(arr[0] * arr[-1])