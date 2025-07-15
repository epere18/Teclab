import pandas as pd
import numpy as np

a = {"c": 17, "a": 65, "b": 34}

valor = pd.Series(a)
print(valor)


b = [[13, 52, 74],
 [81, 53, 48],
 [72, 91, 34]]
d = pd.DataFrame(b)
print(d)

c = np.array([5,4,9,7]) 
e = np.array([3,3,10,5])
f = np.greater(c,e)
print(f)

g = np.array([[21, 33,35,101,329],[53, 131, 53,93,734],[26,42,16,37,102]])
h = g.shape
print(h)