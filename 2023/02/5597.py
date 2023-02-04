import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline


arr = ['x' for _ in range(31)]


for i in range(28):
    arr[int(input())] = '1'

for i in range(1, 31):
  if arr[i] == 'x':
     print(i)
