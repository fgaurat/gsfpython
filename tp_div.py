# -*- coding: utf-8 -*-

from gsf import calcul

import sys
sys.path.append(r'/Users/fgaurat/Dropbox/dev')
# from gsf.calcul_old import division
# from gsf.calcul import division


# /Users/fgaurat/Dropbox/dev/gsf
if __name__ == "__main__":
    print(sys.path)    
    ret = calcul.division(2,2)
    
    print(ret)