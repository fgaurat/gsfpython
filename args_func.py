# -*- coding: utf-8 -*-

def test_args(*arr):
    print(arr)

def test_args_dict(**arr):
    print(arr['nom'])
    print(arr['prenom'])


def test_args_dict2(param1,*arr_pos,**arr_dict):
    print(arr_pos)
    print(arr_dict)

# test_args("val_1")
# test_args("val_1","val_2")

# test_args_dict(nom="DUPONT",prenom="Robert")

test_args_dict2("val_1","val_2","val_3",nom="DUPONT",prenom="Robert")