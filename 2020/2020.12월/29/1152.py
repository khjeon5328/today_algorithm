import sys


sys.stdin = open('input.txt')

word = list(map(str, input().split()))
print(len(word))