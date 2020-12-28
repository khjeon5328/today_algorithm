import sys

sys.stdin = open('input.txt')

N = int(input())
nums = []
nums_dict = {}
for _ in range(N):
    n = int(input())
    nums.append(n)
    if n in nums_dict:
        nums_dict[n] += 1
    else:
        nums_dict[n] = 1
nums.sort()
most = []
m = 0
for k, v in nums_dict.items():
    if v > m:
        m = v
        most = []
        most.append(k)
    elif v == m:
        most.append(k)
print(int(round(sum(nums)/N,0)))
print(nums[N//2])
if len(most) > 1:
    most.sort()
    print(most[1])
else:
    print(most[0])
print(nums[-1] - nums[0])
