def getFibonacci(n):
    '''
    Compute the n-th Fibonacci number using loops only.
    '''
    if n<=0:
        print("Fibonacci sequence only for positive integer")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        fib_1, fib_2 = 0, 1
        for i in range(2,n):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
        return fib_2