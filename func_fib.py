# -*- coding: utf-8 -*-

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):    # write Fibonacci series up to n
    """Return a Fibonacci series up to n."""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a+b
    
    return result


t = fib(2000)
print(type(t))

f = fib2(100)
print(f)