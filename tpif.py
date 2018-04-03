# -*- coding: utf-8 -*-


str_x = input("un nombre :")
x = int(str_x)

# print x==0?"oui":"non"

print("oui" if x==0 else "non")

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')