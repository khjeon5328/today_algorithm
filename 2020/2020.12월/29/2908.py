import sys


sys.stdin = open('input.txt')

a, b = input().split()
num1 = num2 = ''
for i in a:
    num1 = i + num1
for i in b:
    num2 = i + num2
print(max(int(num1), int(num2)))