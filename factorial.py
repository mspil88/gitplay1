def fact(n):
    '''Function for recursively calculating the factorial of a number''' 
    if n < 1:
        return 0
    return n*fact(n-1)
