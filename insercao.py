# -*- coding: utf-8 -*-

from timeit import default_timer as timer
import random

def insertionSort(lista):
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j - 1
        
        while (i >= 0 and lista[i] > chave):
            lista[i+1] = lista[i]
            i = i - 1
        lista[i+1] = chave
    return lista

n = 5000
r = n
lista_ran = random.sample(range(r), n)
lista_ord = list(range(0,n))
lista_des = lista_ord[::-1]




start1 = timer()
print(insertionSort(lista_ran))
end1 = timer()
print("Tempo com lista aleatoria: ")
print(end1 - start1)

start2 = timer()
print(insertionSort(lista_ord))
end2 = timer()
print("Tempo com lista melhor caso: ")
print(end2 - start2)

start3 = timer()
print(insertionSort(lista_des))
end3 = timer()
print("Tempo com lista pior caso: ")
print(end3 - start3)
