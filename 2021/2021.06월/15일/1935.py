import sys

sys.stdin = open('input.txt')

N = int(input())

stack = list(input())


idx = 65
for _ in range(N):
    tmp = input()
    for i in range(len(stack)):
        if stack[i] == chr(idx):
            stack[i] = tmp
    idx += 1
# print(stack)
calc = []
for _ in range(len(stack)):
    tmp = stack.pop(0)
    if tmp.isdigit():
        calc.append(int(tmp))
    elif tmp == '*':
        b = calc.pop()
        a = calc.pop()
        calc.append(a*b)
    elif tmp == '/':
        b = calc.pop()
        a = calc.pop()
        calc.append(a/b)
    elif tmp == '+':
        b = calc.pop()
        a = calc.pop()
        calc.append(a+b)
    elif tmp == '-':
        b = calc.pop()
        a = calc.pop()
        calc.append(a-b)
    # print(calc)
print('{:.2f}'.format(calc[0]))