# -*- coding: utf-8 -*-

squares = [1,4,9,16,25]
cp_squares = squares
cp_squares[0]=123
print(id(squares))
print(id(cp_squares))
print(id(squares[:]))

print(squares)
print(cp_squares)
print(squares[:])


# print(squares[-1])
# print(squares[-1:])

# str="bonjour il fait beau"
# str2=['b','o','n','j']

# arr_str = str.split(" ")
# print (arr_str[0]+arr_str[-1])


a,b = 1,2



print('--------------------------------')
cubes = [1, 8, 27, 65, 125]
print(id(cubes))
cubes.append(216)
print(id(cubes))


a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b