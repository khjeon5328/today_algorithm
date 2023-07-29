import sys

sys.stdin = open('input.txt')

s = sys.stdin.readlines()
for i in s:
    print(i.rstrip())