# -*- coding: utf-8 -*-

from timeit import default_timer as timer
import random

def bubbleSort(lista):
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-1):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista

n = 10000
r = n
lista_ran = random.sample(range(r), n)
lista_ord = list(range(0,n))
lista_des = lista_ord[::-1]

start1 = timer()
print(bubbleSort(lista_ran))
end1 = timer()
print("Tempo com lista aleatoria: ")
print(end1 - start1)

start2 = timer()
print(bubbleSort(lista_ord))
end2 = timer()
print("Tempo com lista melhor caso: ")
print(end2 - start2)

start3 = timer()
print(bubbleSort(lista_des))
end3 = timer()
print("Tempo com lista pior caso: ")
print(end3 - start3)
