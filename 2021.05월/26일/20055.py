import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

N, K = map(int, input().split())

belt = list(map(int, input().split()))
robot = [0] * N

# print(belt)
ans = 1
while True:
    #1.회전
    if robot[-1]:
        robot[-1] = 0
    belt.insert(0,belt.pop())
    robot.pop(-1)
    # print(robot)
    robot.insert(0, 0)
    if robot[-1]:
        robot[-1] = 0
    # print(robot)

    #2.이동
    for i in range(N-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1]:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
    # if belt.count(0) >= K:
    #     print(ans)
    #     return 
    #3.올리기
    if belt[0]:
        belt[0] -= 1
        robot[0] = 1
    if belt.count(0) >= K:
        print(ans)
        break
    else:
        ans += 1
    # print(belt)
    # print(robot)
    # print('-------------------')
            