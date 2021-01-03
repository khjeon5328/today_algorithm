import sys

sys.stdin = open('input.txt')

num = list(input())
num.sort(reverse=True)
print("".join(num))