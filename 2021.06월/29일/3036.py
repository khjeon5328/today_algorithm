import sys
import math

sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

v = arr[0]

for i in range(1, N):
    c = math.gcd(v, arr[i])
    # print(c)
    print(f'{v//c}/{arr[i]//c}')