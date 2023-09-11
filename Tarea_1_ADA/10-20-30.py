"""
Nombre: Daniel Andres Vasquez
Codigo Estudiante: 8963154
"""

"""
Para la realizacion de este punto se utilizo el concepto de cartas explicado por los docentes
y la estructura de datos deque() y set().
"""

from sys import stdin
from collections import deque
import time

start_time = time.time()


"""
En poker_no() lo que se realiza es primero generar las deque() de mazo, pilas y registro que se van
a utilizar, luego se llena la pila con mas deque() vacias y al mazo se le agregan las 52 cartas, posteriormente
se empieza a jugar hasta que ocurra 1 de 3 casos, el mazo o la pila esten vacios, o se detecte que hay un bucle,
despues de eso se agrega cada registro de [mazo,pilas], luego se llena cada pila con una carta, a lo que se procede
a compararar si se pueden sacas cartas, si se puedes seguir sacando se vuelven a sacar hasta que ya no puedas hacer nada
segun los criterios para encontrar las sumas de las cartas que den 10, 20 o 30 , luego se verifica si se a caido en un bucle
y si no se pasa al siguiente bloque y repites el ciclo
"""

def poker_no(mazo):
    registro = set()

    pilas = [deque([]),deque([]),deque([]),deque([]),deque([]),deque([]),deque([])]
    contador = 0
    bucle = 0
    
    while len(mazo) != 0 and len(pilas) != 0 and bucle != 1: 
        pila = 0
    
        while pila < len(pilas) and len(mazo) != 0 and bucle != 1:
            bandera = 0
            registro.add((str(mazo), str(pilas)))
            contador += 1

            pilas[pila].append(mazo.popleft())
            
            while  bandera != 1 and len(pilas[pila]) >= 3 :
                    if pilas[pila][0] + pilas[pila][1] + pilas[pila][-1] == 10 or pilas[pila][0] + pilas[pila][1] + pilas[pila][-1] == 20 or pilas[pila][0] + pilas[pila][1] + pilas[pila][-1] == 30:  
                        mazo.append(pilas[pila].popleft())
                        mazo.append(pilas[pila].popleft())
                        mazo.append(pilas[pila].pop())
                        if len(pilas[pila]) == 0:
                            bandera = 1
                            del pilas[pila]
                            if pila == (len(pilas)):
                                 pila = -1
                            else:
                                pila -= 1
                                    
                    elif pilas[pila][0] + pilas[pila][-2] + pilas[pila][-1] == 10 or pilas[pila][0] + pilas[pila][-2] + pilas[pila][-1] == 20 or pilas[pila][0] + pilas[pila][-2] + pilas[pila][-1] == 30:  
                        mazo.append(pilas[pila].popleft())
                        temporal = pilas[pila].pop()
                        mazo.append(pilas[pila].pop())
                        mazo.append(temporal)
                        
                    elif pilas[pila][-3] + pilas[pila][-2] + pilas[pila][-1] == 10 or pilas[pila][-3] + pilas[pila][-2] + pilas[pila][-1] == 20 or pilas[pila][-3] + pilas[pila][-2] + pilas[pila][-1] == 30:  
                        temporal = pilas[pila].pop()
                        temporal2 = pilas[pila].pop()
                        mazo.append(pilas[pila].pop())
                        mazo.append(temporal2)
                        mazo.append(temporal)
                        
                    else:
                        bandera = 1
            if  (str(mazo), str(pilas)) in registro:
                bucle = 1
            pila += 1

    if bucle == 1:
        print("Draw:", contador)
    elif len(mazo) == 0:
        print("Loss:", contador)
    else:
        print("Win :", contador)
        
"""
En el main() lo que se hace es recibir las entradas, donde se llena la lista mazo con las listas de cartas
hasta que sean 52 en el mazo, donde posterirmente se envian a la funcion poker_no() y se repite lo mismo
hasta que se lea un 0.
"""

def main():
    #cartas = list(map(int,stdin.readline().split()))
    cartas = list( int( x) for x in stdin.readline().split() )
    mazo = deque()
    while cartas[0] != 0:
        mazo.extend(cartas)
        cartas = list( int( x) for x in stdin.readline().split() )
        if len(mazo) == 52:
            poker_no(mazo)
            mazo = deque()
main()
end_time = time.time()
tiempo = end_time - start_time
print(f"Tiempo transcurrido: {tiempo:.6f} segundos")
