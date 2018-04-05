# -*- coding: utf-8 -*-

from gsf import calcul



# from gsf.calcul_old import division
# from gsf.calcul import division


# /Users/fgaurat/Dropbox/dev/gsf
if __name__ == "__main__":

    try:
        ret = calcul.division(2,12)
        print(ret)
        ret = calcul.division(2,0)
        print(ret)
        ret = calcul.division(2,0)
        print(ret)
        ret = calcul.division(2,0)
        print(ret)
        ret = calcul.division(2,0)
        print(ret)
        ret = calcul.division(2,0)
        print(ret)
        
    except ZeroDivisionError as e:
        print('Erreur ! : ZeroDivisionError')
        print(e)
    except Exception as e:
        print('Erreur ! : Exception')
        print(e)
    finally:
        print("Fin")