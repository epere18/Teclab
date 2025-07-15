import pandas as pd
import numpy as np

print("#Consigna 1")
array_3d = np.random.randint(1, 100, size=(2,1,3))
print(array_3d)

print("#Consigna 2")
valor_elemento = array_3d[1, 0, 2]
print(valor_elemento)

print("#Consigna 3")
elementos_nuevos = np.array([[10,11,12]]).reshape(1, 1, 3)
array_3d = np.append(array_3d, elementos_nuevos, axis=0)
print(array_3d)

print("#Consigna 4")
array_dimensionado = array_3d.reshape(3,3)
print(array_dimensionado)
print(array_dimensionado.shape)

print("#Consigna 5")
marcas_productos = pd.Series(['Nike', 'Adidas', 'Puma', 'Reebok', 'Fila'])
print(marcas_productos)

print("#Consigna 6")
colores =  ['Azul', 'Blanco', 'Celeste', 'Negro', 'Rojo']
index = pd.Index(colores)
color_cantidad = pd.Series(range(len(colores)), index=index, name = 'color_cantidad')
print(color_cantidad)
