def fact(n):
    '''Function for recursively calculating the factorial of a number''' 
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n*fact(n-1)
