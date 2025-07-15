import pandas as pd
import numpy as np

array_a = np.array([[1,2,3],[4,5,6]])
array_b = np.array([[10,11,12],[13,14,15]])
array_c = array_a + array_b

# Imprimir el resultado de la suma de los arrays
print("Suma de los arrays:")
print(array_c)

#Consulta de la versión de pandas y numpy
print("Versión de numpy:", np.__version__)
print("Versión de pandas:", pd.__version__)