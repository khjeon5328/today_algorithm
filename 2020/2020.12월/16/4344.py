import sys
sys.stdin = open('input.txt')

N = int(input())

for _ in range(N):
    nums = list(map(int, input().split()))
    n = nums[0]

    avg = sum(nums[1:]) / n
    cnt = 0
    for i in nums[1:]:
        if i > avg:
            cnt += 1
    ans = (cnt/n) * 100
    print('{:.3f}%'.format(ans))