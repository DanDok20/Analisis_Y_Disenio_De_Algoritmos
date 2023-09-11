"""
Nombre: Daniel Andres Vasquez
Codigo Estudiante: 8963154
"""

"""
Para la solucion de este punto se uso unicamente de las notas de estructuras de datos
que se pueden utilizar
"""

from sys import stdin
from heapq import heappush, heappop

"""
En imprimir_lista() lo que se hace basicamente es basicamente unas simples verificaciones
para facilitar la impresion por consola de como se encuentran las colas de prioridas y ademas
del la variable historico donde se encuentra la ultima venta realizada
"""

def imprimir_lista(venta, compra, historico):
  if len(venta) == 0 and len(compra) == 0:
    print("-","-",historico)
  elif len(venta) != 0 and len(compra) == 0:
    print(venta[0][0],"-",historico)
  elif len(venta) == 0 and len(compra) != 0:
    print("-",-compra[0][0],historico)
  else:
    print(venta[0][0],-compra[0][0],historico)

"""
En stock_prices() lo que primero se hace es crear las colas de prioridad que se usaran en cada caso
de prueba para posteriormente recibir cada accion de venta o compra una por una, donde hay dos grandes
bloques para verificar si en esa accion se quiere vender o comprar, luego de la verificacion se realizan los
condicionales donde se pregunta por ejemplo si se quiere vender, primero si la cola de comprar esta o no vacia
para de ese modo agregar directamente a la cola de venta esa venta con [precio, numero acciones], si la cola de
comprar no esta vacia entonces se verifica si hay alguien dispuesto a comprar por el precio de venta o superior,
luego realiza la resta de las acciones que se vendieron y se actualiza en historico, donde en dado caso de que
se pueda seguir vendiendo entonces se vuelve a vender y se actualiza el historico, esta misma metodologia
es para la accion de comprar tambien.
"""    

def stock_prices(acciones):

  venta = []
  compra = []
  historico = "-"
  k = 0
  while k < acciones:
    accion = stdin.readline().strip().split()
    accion[-1], accion[1] = int(accion[-1]), int(accion[1])
    
    if accion[0] == "sell":
      if len(compra) != 0:
        bandera = 0
        acciones_disponibles = accion[1]
        
        while bandera != 1:
          if len(compra) != 0 and -compra[0][0] >= accion[-1]:
            historico = accion[-1]
            operacion = acciones_disponibles - compra[0][1]
            
            if operacion > 0:
              acciones_disponibles -= compra[0][1]
              heappop(compra)
              
            elif operacion < 0:
              compra[0][1] -= acciones_disponibles
              bandera = 1
              
            else:
              heappop(compra)
              bandera = 1
              
          else:
              heappush(venta,[accion[-1], acciones_disponibles])
              bandera = 1
            
      else:
        heappush(venta,[accion[-1], accion[1]])

    elif accion[0] == "buy":
      if len(venta) != 0:
        bandera = 0
        acciones_disponibles = accion[1]
        
        while bandera != 1:
          if len(venta) != 0 and venta[0][0] <= accion[-1]:
            historico = venta[0][0]
            operacion = acciones_disponibles - venta[0][1]
            
            if operacion > 0:
              acciones_disponibles -= venta[0][1]
              heappop(venta)
              
            elif operacion < 0:
              venta[0][1] -= acciones_disponibles
              bandera = 1
              
            else:
              heappop(venta)
              bandera = 1
              
          else:
              heappush(compra,[-accion[-1], acciones_disponibles])
              bandera = 1
            
      else:
        heappush(compra,[-accion[-1], accion[1]])
    
    imprimir_lista(venta, compra, historico)
    k += 1

"""
En el main() se reciben todas las entradas de numeros de casos de prueba
numero de acciones a realizar que es redireccionada a la
funcion de stock_prices()
"""

def main():
  casos = int(stdin.readline().strip())
  i = 0
  while  i < casos:
    acciones = int(stdin.readline().strip())
    stock_prices(acciones)
    i += 1

main()

