# -*- coding: utf-8 -*-

import random
from timeit import default_timer as timer

def selectionSort(lista):
    for i in range(0,len(lista)-1):
        small = i
        for j in range(i+1,len(lista)):
            if (lista[j] < lista[small]):
                small = j
        temp = lista[small]
        lista[small] = lista[i]
        lista[i] = temp
    return lista

n = 10000
r = n
lista_rand = random.sample(range(r),n)
lista_melhor = list(range(0,n))
lista_pior = lista_melhor[::-1]

start1 = timer()
print(selectionSort(lista_rand))
end1 = timer()
print("Tempo com lista aleatoria: ")
print(end1 - start1)

start2 = timer()
print(selectionSort(lista_melhor))
end2 = timer()
print("Tempo com lista melhor caso: ")
print(end2 - start2)

start3 = timer()
print(selectionSort(lista_pior))
end3 = timer()
print("Tempo com lista pior caso: ")
print(end3 - start3)
