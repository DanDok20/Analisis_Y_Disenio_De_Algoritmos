"""
Nombre: Daniel Andres Vasquez Murillo
Codigo: 8963154
"""

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
memoria = {}

def squares(n,a):

    global memoria
    
    respuesta = 0
    if n in memoria: respuesta = memoria[n]
    
    else:
        if n - (a**2) == 0:
            respuesta = 1
        elif n - (a**2) < 0:
            respuesta = squares(n, a - 1)
        else:
            respuesta = squares(n - (a**2 ) , a) + 1
            i = 1
            while  n - ( (a - i) **2 ) > 0 and a - i >= 1:
                respuesta = min( respuesta, (squares(n - ( (a - i) **2 ) , a) + 1) )
                i += 1

        memoria[n] = respuesta
        
    return respuesta

def main():
    casos_prueba = int(stdin.readline())
    
    while casos_prueba > 0:
        valor_n = int(stdin.readline())
        a = (valor_n // 2) + 1
        print(squares(valor_n,a))
        casos_prueba -= 1
    
main()
