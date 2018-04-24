# -*- coding: utf-8 -*-

def soma_quadrados_b(n):
    x= n*(n+1)*(2*n+1)
    x = x/6 
    return x

b = int(sys.argv[1])
print (soma_quadrados_b(b))
