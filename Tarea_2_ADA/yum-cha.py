"""
Nombre: Daniel Andres Vasquez Murillo
Codigo: 8963154
"""

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
memoria = {}

costo_platos = []
puntuacion_platos = []
numero_platos = 0
numero_amigos = 0
presupuesto = 0

def yum_cha(n, x, k):
    global numero_platos
    global costo_platos
    global puntuacion_platos
    global numero_amigos
    global memoria
    global presupuesto

    if (n, x, k) in memoria: 
        respuesta = memoria[(n, x, k)]

    else:
        if (x * 1.1) > presupuesto or k > 2 * ( numero_amigos + 1 ):
             respuesta = float('-inf')
        elif n == numero_platos:
            respuesta = 0
        else:

            precio_plato = (costo_platos[n])
            valoracion_plato = (puntuacion_platos[n] / ( numero_amigos + 1 ))

            respuesta = max( 
                yum_cha( n + 1, x, k),
                yum_cha( n + 1, x + precio_plato, k + 1) + valoracion_plato,
                yum_cha( n + 1, x + ( 2 * precio_plato), k + 2) + (2 * valoracion_plato)
            )

        memoria[(n, x, k)] = respuesta

    return respuesta

def main():
    
    global numero_platos
    global costo_platos
    global puntuacion_platos
    global numero_amigos
    global presupuesto

    numero_amigos, presupuesto, costo_te, numero_platos = map(int, stdin.readline().split())

    while numero_amigos != 0 and presupuesto != 0:
        i = 0
        while i < numero_platos: 

            valores = list(int( x ) for x in stdin.readline().split())
            costo_platos.append(valores[0])
            puntuacion_platos.append(sum(valores[1:]))
            i += 1

        costo_te_servicio = ((costo_te * (numero_amigos + 1)) * 1.10)
        presupuesto = (presupuesto * (numero_amigos + 1)) - costo_te_servicio
        res = yum_cha( 0, 0, 0)
        if res == float('-inf'):
            print( f"{0:.2f}")
        else:
            print( f"{res:.2f}")

        costo_platos = []
        puntuacion_platos = []

        memoria.clear()
        numero_amigos, presupuesto, costo_te, numero_platos = map(int, stdin.readline().split())
main()