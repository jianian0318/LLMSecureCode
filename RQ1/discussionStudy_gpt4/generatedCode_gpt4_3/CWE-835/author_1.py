def getFibonacci(n):
    '''
    Compute the n-th fibonacci number using loops only.
    '''
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        first = 0
        second = 1
        for i in range(2, n):
            temp = first + second
            first = second
            second = temp
    return second