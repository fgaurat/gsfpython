# -*- coding: utf-8 -*-



un_dict = {
    "key_1":"val_1",
    "key_2":"val_2",
    "key_3":"val_3"
    }



the_key = 'key_2'
print(un_dict[the_key])

print(50*'-')

keys = un_dict.keys()

print(keys)
print(50*'-')
for key in keys:
    print(key,un_dict[key])

print(50*'-')

print(un_dict.items())
for k,v in un_dict.items():
    print(k,v)



arr = ['val 1','val 2','val 3']    

for v in arr:
    print(v)

for i in range(0,len(arr)):
    print(i,arr[i])

print(enumerate(arr))
for i,v in enumerate(arr):
    print(i,v)




# arr = [float('toto')]
# print(arr)