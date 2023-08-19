def fibonacci(n, end):
    t1 = 0
    t2 = 1

    if n >= 1:
        print(t1)
    if n >=2:
        print(t2)
    if n > 2:
        for i in range(n-2):
            t3 = t1+t2
            if t3>end:
                break
            t1 = t2
            t2 = t3
            print(t3)

def nth_fibonacci(n):
    t1 = 0
    t2 = 1

    if n == 1:
        return t1
    if n ==2:
        return t2
    if n > 2:
        for i in range(n-2):
            t3 = t1+t2
            t1 = t2
            t2 = t3
        return t3



fibonacci(20,100)
n = nth_fibonacci(10)
print(n)


