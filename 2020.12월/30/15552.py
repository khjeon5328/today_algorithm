
sys.stdin = open('input.txt')
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    n1, n2 = sys.stdin.readline().rstrip().split()
    print(int(n1) + int(n2))