"""

from sys import stdin

respuesta = None


def vuelta_rezagado(x, y, min, max, mitad):
  global respuesta
  if min + 1 == max:
    if (x * min) < (y * (min - 1)): respuesta = min
    else: respuesta = max

  else:
    if (x * mitad) > (y * (mitad - 1)):
      centro = mitad + ((max - mitad) >> 1)
      vuelta_rezagado(x, y, mitad, max, centro)
    elif (x * mitad) < (y * (mitad - 1)):
      centro = min + ((mitad - min) >> 1)
      vuelta_rezagado(x, y, min, mitad, centro)
  return respuesta

def main():
  line = stdin.readline().strip()
  while line != "":
    min, max = map(int, line.split())
    mitad = 2 + ((max - 2) >> 1)
    print(vuelta_rezagado(min, max, 2, max, mitad))
    line = stdin.readline()

main()
"""

inv = 0

def merge(A, min, medio, max):
  global inv
  global tmp
  n1 = medio - min - 1
  for i in range(min, max): tmp[i] = A[i]
  i, j = min, medio
  for k in range(min, max):
    if i == medio: A[k], j = tmp[j], j + 1
    elif j == max: A[k], i = tmp[i], i + 1
    else:
      if tmp[i] <= tmp[j]:
        A[k] = tmp[i]
        i += 1
      else:
        A[k] = tmp[j]
        j += 1
        inv += (n1 - i) + 1


def mergesort(A, min, max):
  if min + 1 < max:
    medio = min + ((max - min) >> 1)
    mergesort(A, min, medio)
    mergesort(A, medio, max)
    merge(A, min, medio, max)


cantidad = i
nt(input())
while cantidad != 0:
  A = []
  inv = 0
  for i in range(cantidad):
    A.append(int(input()))
  tmp = list(range(len(A)))
  mergesort(A, 0, len(A))
  print(inv)
  cantidad = int(input())

#######

def duathlon(low, hi, mitad, kilometros, competidores, A, ventaja):
  print(hi, low, kilometros, mitad, competidores, A)
  r = mitad
  k = kilometros - mitad

  #mitad = 0 + ((kilometros - 0) >> 1)

  if low + 1 == hi:
    print("Esta es la buena", ventaja, r, k)

  else:
    competidor_rapido1 = float("inf")
    tramposo1 = ((r / A[competidores - 1][0]) * 60**2) + (
        (k / A[competidores - 1][1]) * 60**2)
    for i in range(competidores - 1):
      tiempo_competidor = ((r / A[i][0]) * 60**2) + ((k / A[i][1]) * 60**2)
      if tiempo_competidor < competidor_rapido1:
        competidor_rapido1 = tiempo_competidor
    print("A", tramposo1, competidor_rapido1)
    ventaja1 = competidor_rapido1 - tramposo1
    #print(ventaja1)

    competidor_rapido2 = float("inf")
    #centro = mitad + ((hi - mitad) >> 1)
    tramposo2 = (((r + 1) / A[competidores - 1][0]) * 60**2) + (
        ((k - 1) / A[competidores - 1][1]) * 60**2)
    for i in range(competidores - 1):
      tiempo_competidor = (((r + 1) / A[i][0]) * 60**2) + ((
          (k - 1) / A[i][1]) * 60**2)
      if tiempo_competidor < competidor_rapido2:
        competidor_rapido2 = tiempo_competidor
    print("B", tramposo2, competidor_rapido2)
    ventaja2 = competidor_rapido2 - tramposo2
    #print(ventaja2)
    """
    competidor_rapido3 = float("inf")
    centro = 0 + ((mitad - 0) >> 1)
    tramposo3 = ((r - centro / A[competidores - 1][0]) * 60**2) + (
        (k - 1 / A[competidores - 1][1]) * 60**2)
    for i in range(competidores - 1):
      tiempo_competidor = (((r - 1) / A[i][0]) * 60**2) + ((
          (k - 1) / A[i][1]) * 60**2)
      if tiempo_competidor < competidor_rapido3:
        competidor_rapido3 = tiempo_competidor
    print("C", tramposo3, competidor_rapido3)
    ventaja3 = competidor_rapido3 - tramposo3
    #print(ventaja2)
    """
    print("ventajas", ventaja1, ventaja2)
    if ventaja2 > ventaja1:
      centro = mitad + ((hi - mitad) >> 1)
      duathlon(mitad, hi, centro, kilometros, competidores, A, ventaja2)
    else:  #elif ventaja3 >= ventaja1:
      centro = low + ((mitad - low) >> 1)
      duathlon(low, mitad, centro, kilometros, competidores, A, ventaja1)
    
A = { 0:[10,40], 1:[20, 30], 2:[15, 35]}
duathlon(0, 100, 50, 100, 3, A, 0)
