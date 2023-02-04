import sys

sys.stdin = open('input.txt')

N = int(input())
# print(N)
def han(n):
    nums = []
    while n:
        a, b = divmod(n, 10)
        nums.append(b)
        n = a
    isHan = True
    if len(nums) > 2:
        isDiff = nums[0] - nums[1]
        for i in range(2, len(nums)):
            diff = nums[i-1] - nums[i]
            if isDiff != diff:
                isHan = False
                break
    return isHan
        

cnt = 0
for i in range(1, N+1):
    if han(i):
        cnt +=1
print(cnt)