def fib(outreach):
    a,b = 0,1
    while a < outreach:
        if not a % 2:
            yield a
        a,b = b,a+b

dhruv = sum(fib(4000000))
print(dhruv)