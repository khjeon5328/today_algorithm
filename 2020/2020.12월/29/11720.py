import sys

sys.stdin = open('input.txt')

N = int(input())
nums = map(int, input())
print(sum(nums))