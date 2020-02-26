# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:08:22 2020

@author: chach
"""

import random

n_num=10

randomlist=random.sample(range(0,100),n_num)
listaordenada=sorted(randomlist)
invertedlist=sorted(listaordenada,reverse=True)
ultimo=invertedlist[0]
listaquasi=listaordenada
listaquasi.insert(0,ultimo)
listaquasi.pop()
listaordenada=sorted(listaquasi)
listaalterna=[None]*n_num
for i in range(0,int(n_num/2)):
    listaalterna[2*i]=listaordenada[i]
    listaalterna[2*i+1]=listaordenada[-i-1]




#if __name__ == "__main__"
    
