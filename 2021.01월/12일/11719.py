import sys

sys.stdin = open('input.txt')

ans = sys.stdin.readlines()

for i in ans:
    print(i.rstrip())