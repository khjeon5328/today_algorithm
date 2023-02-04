import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

ans = 0
for i in range(5):
    x = int(input())
    if  x < 40:
        x = 40
    
    ans += x

print(int(ans / 5))