import sys

sys.stdin = open('input.txt')

s = input()
nums = []
for i in s:
    if ord(i) > 86:
        nums.append(9)
    elif ord(i) > 83:
        nums.append(8)
    elif ord(i) > 79:
        nums.append(7)
    elif ord(i) > 76:
        nums.append(6)
    elif ord(i) > 73:
        nums.append(5)
    elif ord(i) > 70:
        nums.append(4)
    elif ord(i) > 67:
        nums.append(3)
    else:
        nums.append(2)
print(sum(nums) + len(nums))
