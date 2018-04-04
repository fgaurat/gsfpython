# -*- coding: utf-8 -*-

def f(a, L=[]):
    L.append(a)
    return L

a = f(1)
print(a)

a = f(2)
print(a)

a = f(3)
print(a)


print(50*'-')

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


ret_a = f2(1)
print(ret_a)

ret_a = f2(2,ret_a)
print(ret_a)

ret_a = f2(3,ret_a)
print(ret_a)
