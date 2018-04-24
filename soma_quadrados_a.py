# -*- coding: utf-8 -*-

def soma_quadrados_a(n):
    x = 0
    for j in range(1,n+1):
        x = x + j*j
    return x
	
b = int(sys.argv[1])
print (soma_quadrados_a(b))
