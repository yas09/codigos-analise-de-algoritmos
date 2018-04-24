# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 14:23:43 2018

@author: Yasmin
"""
# Quicksort recursivo com pivô elemento do meio
import sys
from timeit import default_timer as timer
import random

global num   
global troca_cont
global comp_cont

# num é o número de testes   
num = 5         
# entradas é a lista de tamanhos de entrada
entradas = [1,10,100]  
n = len(entradas)
# Contador de trocas
troca_cont = 0
# Contador de Comparações
comp_cont = 0 

# Listas de teste: aleatória, crescente e decrescente
    
arraysRan = [None] * n 
arraysCres = [None] * n
arraysDec = [None] * n
for i in range (0, n):  
    arraysRan[i] = list(random.sample(range(entradas[i]), entradas[i]))
for i in range (0, n):
    arraysCres[i] = list(range(0, entradas[i]))
for i in range (0, n):
    arraysDec[i] = list(range(entradas[i],-1,-1))

# Abre log de testes
sys.stdout = open("logA.txt","w")

#-- Algoritmo 
def quickSort(arr, l, r):
      
    if l >= r:
        incComparacoes()            #
        return
    part = particionar(arr, l, r)
    if l < (part - 1):
        incComparacoes()            #
        quickSort(arr, l, part - 1)
        
    if part < r: 
        incComparacoes()            #
        quickSort(arr, part, r)

def particionar(arr, l, r):
    i = l
    j = r
    m = int((l+r)/2)
    pivot = arr[m]
    
    while i <= j:
        while arr[i] < pivot:
            incComparacoes()        #
            i = i + 1
        while arr[j] > pivot:
            incComparacoes()        #
            j = j - 1
        if i <= j:
            incComparacoes()        #
            incTrocas()             #
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i = i + 1
            j = j - 1
    return i
#-- Fim algoritmo

# Incrementa o contador de trocas
def incTrocas():
    global trocas_cont
    trocas_cont += 1
    
# Zera o contador de trocas para o próximo teste
def zerarTrocas():
    global trocas_cont
    trocas_cont = 0
    
# Incrementa o contador de comparações
def incComparacoes():
    global comp_cont
    comp_cont += 1
    
# Zera o contador de comparações para o próximo teste
def zerarComparacoes():
    global comp_cont
    comp_cont = 0

# Executa N testes em cima de um determinado vetor
def run(arr, N):
# Vetor de tempos de execução
    runtimes = [None]*N
# Vetor de números de trocas
    trocas = [None]*N
# Variáveis para cálculo da média
    comps = [None]*N
    avg_runtime = 0
    avg_troca = 0
    avg_comp = 0
    n = len(arr)
 
    for i in range(0, N):
        # Faz cópia do vetor de referência
        vetor = list(arr)
        print("\nTESTE #", i + 1, "")
        print("\n[Antes]: ",  vetor)
        
        # Cálculo do tempo de Execução
        start = timer()
        quickSort(vetor,0,n-1)
        end = timer()
        runtimes[i] = end - start
        trocas[i] = troca_cont
        comps[i] = comp_cont
        print("[Trocas]: ", trocas[i])
        print("[Comparações]: ", comps[i])
        
        
        zerarTrocas()               #
        zerarComparacoes()          #
        
        print("[Tempo Execução]: ", runtimes[i])
        avg_runtime += runtimes[i]
        avg_troca += trocas[i]
        avg_comp += comps[i]
        print("[Depois]: ", vetor)

    print("\n[RESULTADOS DOS TESTES]: ")
    print("[Média Tempo Execução]: ", avg_runtime/N)
    print("[Média Trocas]: ", avg_troca/N)
    print("[Média Comparações]: ", avg_comp/N)

# ...
print("--- QUICKSORT RECURSIVO PIVÔ NO MEIO ---")
print("\n\n#### LISTA ALEATÓRIA ")
for i in range(0, len(arraysRan)):    
    print("\n## Execução lista ", entradas[i], " caracteres ")
    run(arraysRan[i], num)


print("\n\n#### LISTA CRESCENTE ")
for i in range(0, len(arraysCres)):
    print("\n## Execução lista ", entradas[i], " caracteres ")
    run(arraysCres[i], num)

print("\n\n#### LISTA DECRESCENTE ")
for i in range(0, len(arraysDec)):
    print("\n## Execução lista ", entradas[i], " caracteres ")
    run(arraysDec[i], num)

# Fecha log dos testes
sys.stdout.close()



