# -*- coding: utf-8 -*-

def division(a,b):
    if b == 12:
        try:
            raise Exception("Div by 12")
        finally:
            print("erreur interne")
    return a/b


if __name__ == "__main__":
    result = division(1,2)
    print(result)