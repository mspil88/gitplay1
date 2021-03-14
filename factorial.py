def fact(n):
    if n < 1:
        return 0
    return n*fact(n-1)