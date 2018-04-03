# -*- coding: utf-8 -*-

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')



a = ['a','b','c']

for i in range(20):
    if(i<10):
        print(i)
    else:
        break
else:
    print ("ok")