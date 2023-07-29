import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())


for i in range(n):
    tmp = input().strip()
    # print(tmp)
    print(tmp[0]+ tmp[-1])
    # print(tmp[0], tmp[-2])