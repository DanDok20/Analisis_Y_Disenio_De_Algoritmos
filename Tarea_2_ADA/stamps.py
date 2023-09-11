"""
Nombre: Daniel Andres Vasquez Murillo
Codigo: 8963154
"""

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
memoria = {}
max_estampillas = 0
valores_estampillas = []
numero_estampillas = 0

def stamps(n, x):
    global valores_estampillas
    global max_estampillas
    global memoria
    global numero_estampillas

    respuesta = 0
    if (n,x) in memoria: respuesta = memoria[(n,x)]
    else:
        if x == 0:
            respuesta = 0
        elif n == numero_estampillas:
            respuesta = stamps( n, x - 1) + 1
        else:
            if valores_estampillas[n] <= x:
                respuesta = min( stamps( n + 1, x ), stamps( n + 1, x - valores_estampillas[n] ) + 1, stamps( n, x - valores_estampillas[n] ) + 1 )
            elif valores_estampillas[n] > x:
                respuesta = stamps( n + 1, x )
        memoria[(n, x)] = respuesta
    return respuesta

def comparacion_conjunto_estampillas(A, B):
    mejor_conjunto = 1
    respuesta = B
    tamaño = len(A) - 1
    while tamaño > 0 and mejor_conjunto == 1:
        if A[tamaño] < B[tamaño]:
            respuesta = A
            mejor_conjunto = 0
        elif B[tamaño] < A[tamaño]:
            respuesta = B
            mejor_conjunto = 0
        tamaño -= 1

    return respuesta
def main():
    global max_estampillas, valores_estampillas, numero_estampillas, memoria
    max_estampillas = int(stdin.readline())
    
    while max_estampillas != 0:
        
        ultimo_valor_sin_repeticion = 0

        conjuntos_estampillas = int(stdin.readline())

        respuesta = [-1, float('inf'), float('inf')]

        while conjuntos_estampillas > 0:

            valores_estampillas = list(int( x ) for x in stdin.readline().split())
            numero_estampillas = valores_estampillas.pop(0)

            covertura_maxima = stamps(0, ultimo_valor_sin_repeticion)
            while covertura_maxima <= max_estampillas:
                ultimo_valor_sin_repeticion += 1
                covertura_maxima = stamps(0, ultimo_valor_sin_repeticion)
            
            ultimo_valor_sin_repeticion -= 1

            if ultimo_valor_sin_repeticion > respuesta[0]:
                respuesta = [ultimo_valor_sin_repeticion, valores_estampillas, numero_estampillas]

            elif ultimo_valor_sin_repeticion == respuesta[0]:
                if numero_estampillas == respuesta[2]: 
                    res = comparacion_conjunto_estampillas(valores_estampillas, respuesta[1])
                    respuesta = [ultimo_valor_sin_repeticion, res, numero_estampillas]
                elif numero_estampillas < respuesta[2]: 
                    respuesta = [ultimo_valor_sin_repeticion, valores_estampillas, numero_estampillas]

            conjuntos_estampillas -= 1
            ultimo_valor_sin_repeticion = 0
            memoria.clear()
        
        print(f"max coverage = {respuesta[0]:3} : {' '.join(map(lambda x: f'{x:2}', respuesta[1]))}")
        max_estampillas = int(stdin.readline())
    
main()
