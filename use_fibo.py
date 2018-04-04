# -*- coding: utf-8 -*-
# import fibo
from fibo import fib, fib2
import sys



if __name__ == "__main__":
    print(sys.argv)
    
    # arg = sys.argv[1]    
    arg = int(sys.argv[1])
    fib(arg)

