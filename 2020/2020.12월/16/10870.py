def fibo(n):
    if n == 1 or n==0:
        return n
    return fibo(n-2) + fibo(n-1)

n = int(input())

if not n:
    print(0)
elif n == 1:
    print(1)
else:
    print(fibo(n))