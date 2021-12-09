import numpy as np
import random
datos = np.array([[0,0,0],
          [0,1,0],
          [1,0,0],
          [1,1,1]])

syn = np.array([random.uniform(-1,1),
                random.uniform(-1,1),
                random.uniform(-1,1)])
#aprendizaje
entrenamiento = True
salida = 0
iteracion = 0
aprende = 0.3
iteraciones = 0

while(entrenamiento == True):
  iteracion = iteracion + 1
  entrenamiento = False
  
  for cont in range(0,4):
    #formula s=f(e1*pi + e2*p2+1*p3)
    salida1 = (datos[cont][0]*syn[0]+datos[cont][1]*syn[1]+ 1* syn[2])
    if salida1 > 0:
      salida = 1
    else:
      salida = 0
    error = int(datos[cont][2] - salida)
    if (error != 0):
      syn[0] = syn[0] + (aprende * error * datos[cont][0])
      syn[1] = syn[1] + (aprende * error * datos[cont][1])
      syn[2] = syn[2] + (aprende * error * 1)
      entrenamiento = True

print("iteracion:" , iteracion)
print(syn[0])
print(syn[1])
print(syn[2])

for cont in range (0,4):
  salida1 = datos[cont][0]*syn[0] + datos[cont][1]*syn[1] + syn[2]
  if salida1 > 0:
    salida = 1
  else:
    salida =0

  print( "[",datos[cont][0] ,datos[cont][1] ,datos[cont][2] ," " ,salida,"]")
