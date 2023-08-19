def print_prime_numbers(start, end):
    if start>end:
        print("Invalid start and end")
    else:
        for n in range(start, end):
            k = 0
            for i in range(2,int(n/2)+1):
                if n%i == 0:
                    k = 1
                    break
            if k==0 and n!=1:
                print(n)

print_prime_numbers(1,30)