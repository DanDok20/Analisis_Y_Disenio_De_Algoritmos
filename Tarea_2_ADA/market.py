"""
Nombre: Daniel Andres Vasquez Murillo
Codigo: 8963154
"""

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
memoria = {}

precio_acciones = []
dias = 0
tasa_compra = 0

def market(n, k):

    global memoria
    global precio_acciones
    global dias
    global tasa_compra

    respuesta = 0

    if (n,k) in memoria: respuesta = memoria[(n, k)]
    else:
        if n == dias:
            respuesta = 0
        else:
            if k == 1:
                respuesta = max( market(n + 1, 0) - precio_acciones[n] - tasa_compra, market(n + 1, 1)  )
            else:
                respuesta = max( market(n + 1, 0), market(n + 1, 1) + precio_acciones[n])
        
        memoria[(n,k)] = respuesta

    return respuesta

def main():
    
    lectura = stdin.readline().strip()
    global precio_acciones
    global dias
    global tasa_compra 
    global memoria

    while lectura != "":
        dias, tasa_compra = map(int, lectura.split())
        precio_acciones = list(int( x ) for x in stdin.readline().split())
        print(market(0, 1))
        memoria.clear()
        lectura = stdin.readline().strip()
main()
