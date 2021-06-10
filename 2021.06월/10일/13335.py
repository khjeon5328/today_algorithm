import sys


sys.stdin = open('input.txt')

N, W, L = map(int, input().split())

from collections import deque
trucks = list(map(int, input().split()))

bridge = deque([0] * W)
# print(bridge)
time = 0
load = 0
while len(trucks) or load:
    # print(time, load, bridge)
    exit = bridge.popleft()
    load -= exit
    if load < L and len(trucks) and load + trucks[0] <= L:
        truck = trucks.pop(0)
        load += truck
        bridge.append(truck)
    else:
        bridge.append(0)
    time += 1


print(time)
