"""
Nombre: Daniel Andres Vasquez
Codigo Estudiante: 8963154
"""

from sys import stdin

"""
En la funcion vuelta_rezagado() lo que se hace es aplicar de manera recursiva el
algoritmo de busqueda binaria, desarrollado mediante los conceptos vistos en clase
donde el caso base es cuando low + 1 == hi, lo que hace no se pueda seguir dividiendo,
donde posteriormente se verifica la condicion para saber si el piloto mas lento ya esta
rezagado y se decide las vueltas minimas que tiene que dar el piloto mas rapido para rezagar
al mas lento. 
"""

def vuelta_rezagado(x, y, low, hi, mitad):
  if low + 1 == hi:
    if (x * low) <= (y * (low - 1)):
      print(low)
      
    else: print(hi)
    
  else:
    if (x * mitad) >= (y * (mitad - 1)):
      centro = mitad + ((hi - mitad) >> 1)
      vuelta_rezagado(x, y, mitad, hi, centro)
      
    elif (x * mitad) < (y * (mitad - 1)):
      centro = low + ((mitad - low) >> 1)
      vuelta_rezagado(x, y, low, mitad, centro)

"""
En el main() lo que se hace basicamete es pedir las entradas que en este caso son
pares de numeros que unicamente para de recibir entradas cuando encuentra una linea
vacia, por otro lado teniendo como base el algoritmo de busqueda binaria, se tiene un low y hi, donde
low empieza siendo 2 dado a que esas son las minimas vueltas que se pueden hacer para
ganar, y estas dos variables se envian junto con las velocidades de los pilotos y
la mitad entre low y hi a la funcion vuelta_rezagado()
"""
def main():
  line = stdin.readline().strip()
  while line != "":
    low, hi = map(int, line.split())
    mitad = 2 + ((hi - 2) >> 1)
    vuelta_rezagado(low, hi, 2, hi, mitad)
    line = stdin.readline().strip()

main()
