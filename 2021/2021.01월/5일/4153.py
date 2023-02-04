import sys

sys.stdin = open('input.txt')

while True:
    nums = []
    a, b, c = map(int, input().split())
    nums.append(a)
    nums.append(b)
    nums.append(c)
    if a == b == c == 0:
        break
    nums.sort()
    if nums[-1]**2 == nums[-2]**2 + nums[-3]**2:
        print('right')
    else:
        print('wrong')    