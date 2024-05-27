def getFibonacci(n):
    '''
    Compute the n-th fibonacci number using loops only.
    '''
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
