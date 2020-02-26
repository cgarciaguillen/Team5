# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:06:34 2020

@author: Usuario
"""

#from archivo import suma

#def suma(x,y):
 #   return x+y

#if __name__ =='__main__':
 #   print('esto es un test')
 #   for i in range(10):
 #       print(i)
 #   print(suma(3,4))
 #   print(suma(2,5))
########################################### 
#creame una lista de numeros aleatorios
###########################################
 
import random
blist = random.sample(range(10,30),10)
print(blist)

###########################################
#ordename la siguiente lista
###########################################
 
#alist = [9,4,7,3,6,4,2,1,6,8,4,8,6,7,8]
#print(alist[:])
#alist = [9,4,7,3,6,4,2,1,6,8,4]
alist[:]=blist[:]

def ordenamealist(alist):
    for i in range(len(alist)):
        least=i
        for j in range(i+1,len(alist)):
            if alist[j]<alist[least]:
                least=j
        x(alist,least,i)
def x(A,v,b):
    aux=A[v]
    A[v]=A[b]
    A[b]=aux
    
#alist = [9,4,7,3,6,4,2,1,6,8,4,8,6,7,8]
#print(blist)
ordenamealist(alist)
print (alist[:])

###########################################
#creame una lista quasi ordenada
###########################################



