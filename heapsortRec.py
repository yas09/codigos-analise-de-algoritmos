# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 14:23:43 2018

@author: Yasmin
"""
# Teste

import sys
from timeit import default_timer as timer
import random

global num   
global trocas_cont
global comps_cont

# num é o número de testes   
num = 5         
# entradas é a lista de tamanhos de entrada
entradas = [1,10,100]  
n = len(entradas)
# Contador de trocas
trocas_cont = 0
# Contador de Comparações
comps_cont = 0 

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
sys.stdout = open("logC.txt","w")

#-- Algoritmo 
def constroiHeap(arr, n, i):
    # Encontra maior valor entre raiz e folhas
    maior = i
    l = 2 * i + 1
    r = 2 * i + 2 
 
    if l < n and arr[i] < arr[l]:
        incComparacoes()                        #
        maior = l
 
    if r < n and arr[maior] < arr[r]:
        incComparacoes()                        #
        maior = r
 
    # Se raiz não é o valor maior, troca pelo maior e continua construindo o heap
    if maior != i:
        incComparacoes()                        #
        incTrocas()                             #
        arr[i], arr[maior] = arr[maior], arr[i]
        constroiHeap(arr, n, maior)
        
 
def heapSort(arr):
    n = len(arr) 
 
    # Constrói heap máximo
    for i in range(n, -1, -1):
        constroiHeap(arr, n, i)
 
    for i in range(n-1, 0, -1):
        # Troca
        incTrocas()                             #
        arr[i], arr[0] = arr[0], arr[i]  
        # Heap do elemento raiz
        constroiHeap(arr, i, 0)
 
# -- Fim Algoritmo

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
    global comps_cont
    comps_cont += 1
    
# Zera o contador de comparações para o próximo teste
def zerarComparacoes():
    global comps_cont
    comps_cont = 0


# Executa N testes em cima de um determinado vetor
def run(arr, N):
    # Vetor de tempos de execução
    runtimes = [None]*N
    # Vetor de número de trocas
    trocas = [None]*N
    # Vetor de número de comparações
    comps = [None]*N

    # Variáveis para cálculo da média
    avg_runtime = 0
    avg_troca = 0
    avg_comp = 0
 
 
    for i in range(0, N):
        # Faz cópia do vetor de referência
        vetor = list(arr)
        print("\nTESTE #", i + 1, "")
        print("\n[Antes]: ",  vetor)
        
        # Cálculo do tempo de Execução
        start = timer()
        heapSort(vetor)
        end = timer()
        runtimes[i] = end - start
        trocas[i] = trocas_cont
        comps[i] = comps_cont
        print("[Trocas]: ", trocas[i])
        print("[Comparações]: ", comps[i])
        
        # Zerar variáveis globais trocas e comps
        zerarTrocas()
        zerarComparacoes()
        
        # Exibir resultado e médias dos testes
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
print("--- HEAPSORT RECURSIVO ---")
print("\n\n#### LISTA ALEATÓRIA ")
for i in range(0, len(arraysRan)):    
    print("\n## EXECUÇÃO LISTA ", entradas[i], " CARACTERES ")
    run(arraysRan[i], num)


print("\n\n#### LISTA CRESCENTE ")
for i in range(0, len(arraysCres)):
    print("\n## EXECUÇÃO LISTA ", entradas[i], " CARACTERES ")
    run(arraysCres[i], num)

print("\n\n#### LISTA DECRESCENTE ")
for i in range(0, len(arraysDec)):
    print("\n## EXECUÇÃO LISTA ", entradas[i], " CARACTERES ")
    run(arraysDec[i], num)

sys.stdout.close()



