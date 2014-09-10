def task():
  """
  obtener el numero de minutos en una semana
  ejemplo:
  >>> task()
  10080
  """
  return 60*24*7


def task2():
  """
  obtener la division el modulo de 2304811 entre 47
  ejemplo:
  >>> task2()
  25
  """
  return 2304811 - (2304811 // 47 )* 47 
 
def task3():
  """
  verifica si la suma de dos umeros es divisible entre 3
  ejemplo:
  >>> task3()
  False
  """
  return ((673 + 909) % 3) == 0

def task4():
  """
  definicion de condiciones
  ejemplo:
  >>> task4()
  1.0
  """
  return 2**((1.0 / 2.0 ) + 1.0 / 2.0 ) if -9 +10 < 0 else 2**((1.0/2.0)-1.0/2.0)

def task5():
  """
  obtener la raiz d el os primeros 5 numero positivos
  ejemplo:
  >>> task5()
  {16, 1, 9, 25, 4}
  """
  import math
  return {x**2 for x in {1,2,3,4,5}}

def task6():
  """
  obtener el cuadrado de los primeros 5 numero reales
  ejemplo:
  >>> task6()
  {0.0, 1.0, 9.0, 16.0, 4.0}
  """
  import math
  return {math.pow(x,2) for x in {0,1,2,3,4}}

def task7():
  """
  Usando la compresion para filtrar remplazar los arreglos con dos nuevos
  de tal manera que obtengas 9 elementos
  ejemplo:
  >>> task7()
  9
  """
  return len({x*y for x in {4,5,6} for y in {7,8,9} })

def task8():
  """
  Reemplazar el anterior para que contenga 5 elementos
  ejemplo:
  >>> task8()
  5
  """
  return len({x*y for x in {1,9,3} for y in {2,6,18} })

def task9():
  """
  Obtener el resultado de la intersecccion de dos arreglos sin usar el &
  ejemplo:
  >>> task9()
  {3, 4}
  """
  return {x for x in {1,2,3,4} for y in {3,4,5,6} if x==y }

def task10():
  """
  obtener el promedio de un arreglo
  ejemplo:
  >>> task10()
  30.0
  """
  return sum([20, 10, 15, 75]) / len([20, 10, 15, 75])

def task11():
  """
  crear listas compuestas de letras y numeros
  ejemplo:
  >>> task11()
  [['A', 1], ['A', 2], ['A', 3], ['B', 1], ['B', 2], ['B', 3], ['C', 1], ['C', 2], ['C', 3]]
  """
  return [[x,y] for x in ["A", "B", "C"] for y in [1,2,3]]

def task12():
  """
  evaluar elementos en una lista
  ejemplo:
  >>> task12()
  16.1
  """
  return sum([sum(x) for x in [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]])

def task14():
  """
  Dado un arreglo, obtener una lista de tres tuplas, dado que la suma de los elementos sea cero
  ejemplo:
  >>> task14()
  [(0, 0, 0), (0, 2, -2), (0, -2, 2), (1, 1, -2), (1, -2, 1), (2, 0, -2), (2, 2, -4), (2, -4, 2), (2, -2, 0), (-4, 2, 2), (-2, 0, 2), (-2, 1, 1), (-2, 2, 0)]
  """
  return [(i,j,k) for i in {-4, -2, 1, 2, 5, 0} for j in {-4, -2, 1, 2, 5, 0} for k in {-4, -2, 1, 2, 5, 0} if i+j+k==0]
 
def task15():
  """
  Modificar el programa anterior de tal manera que no se muestre la tupla (0,0,0)
  ejemplo:
  >>> task15()
  [(0, 2, -2), (0, -2, 2), (1, 1, -2), (1, -2, 1), (2, 0, -2), (2, 2, -4), (2, -4, 2), (2, -2, 0), (-4, 2, 2), (-2, 0, 2), (-2, 1, 1), (-2, 2, 0)]
  """
  return [(i,j,k) for i in {-4, -2, 1, 2, 5, 0} for j in {-4, -2, 1, 2, 5, 0} for k in {-4, -2, 1, 2, 5, 0} if (i+j+k==0) and ([i,j,k]!=[0,0,0])]
   
def task16():
  """
  obtener laprimera tupla del programa anterior
  ejemplo:
  >>> task16()
  (0, 2, -2)
  """
  return [(i,j,k) for i in {-4, -2, 1, 2, 5, 0} for j in {-4, -2, 1, 2, 5, 0} for k in {-4, -2, 1, 2, 5, 0} if (i+j+k==0) and ([i,j,k]!=[0,0,0])] [0]   

def task20():
  """
  Crear un nuevo arreglo que contenga la suma de los numeros de cada arreglo como parametro
  ejemplo:
  >>> task20()
  [11, 40, 60]
  """
  arreglo1 = [10, 25, 40]
  arreglo2 = [1, 15, 20]
  return [x+y for (x,y) in zip(arreglo1, arreglo2)]

def task23():
  """
  Usando rango escribe la comprension del valor de un diccionario
  ejemplo:
  >>> task23()
  {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400, 21: 441, 22: 484, 23: 529, 24: 576, 25: 625, 26: 676, 27: 729, 28: 784, 29: 841, 30: 900, 31: 961, 32: 1024, 33: 1089, 34: 1156, 35: 1225, 36: 1296, 37: 1369, 38: 1444, 39: 1521, 40: 1600, 41: 1681, 42: 1764, 43: 1849, 44: 1936, 45: 2025, 46: 2116, 47: 2209, 48: 2304, 49: 2401, 50: 2500, 51: 2601, 52: 2704, 53: 2809, 54: 2916, 55: 3025, 56: 3136, 57: 3249, 58: 3364, 59: 3481, 60: 3600, 61: 3721, 62: 3844, 63: 3969, 64: 4096, 65: 4225, 66: 4356, 67: 4489, 68: 4624, 69: 4761, 70: 4900, 71: 5041, 72: 5184, 73: 5329, 74: 5476, 75: 5625, 76: 5776, 77: 5929, 78: 6084, 79: 6241, 80: 6400, 81: 6561, 82: 6724, 83: 6889, 84: 7056, 85: 7225, 86: 7396, 87: 7569, 88: 7744, 89: 7921, 90: 8100, 91: 8281, 92: 8464, 93: 8649, 94: 8836, 95: 9025, 96: 9216, 97: 9409, 98: 9604, 99: 9801}
  """
  return {x:x**2 for x in range(100)}

def task24():
  """
  Escribe los valores en un diccionario que represente la identidad de la funcion sobre D
  ejemplo:
  >>> task24()
  {'white': 'white', 'blue': 'blue', 'red': 'red'}
  """
  H = {'red','white','blue'}
  return {H:H for H in {'red','white','blue'}}

def task26():
  """
  escribir un dicccionario para mapear el nombre del empleado al salario
  ejemplo:
  >>> task26()
  {'Moe': 990, 'Larry': 1000.0, 'Curly': 1200.5}
  """
  d = {0:1000.0, 3:990, 1:1200.50}
  names = ['Larry', 'Curly', 'Moe']
  return {n:v for (n,v) in list(zip(names,list(d.values())))}

def task29(L):
  """
  definir un procedimiento cubes L que contenga input y output
  ejemplo:
  >>> task29([1,2,3])
  [1,8,27]
  """
  return [x**3 for x in L]