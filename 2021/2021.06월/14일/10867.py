import sys

sys.stdin = open('input.txt')
N = int(input())
lst = list(map(int, input().split()))
lst.sort()
lst = set(lst)
print(*lst)