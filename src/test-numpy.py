import numpy as np

matrix = np.array([[1.,0.,0.],[0.,1.,2.]])
print("Dimensionalität:", matrix.ndim)
print("# rows:", matrix.shape)
matrix.resize(4,6)
print("Matrix:",matrix)

# zu Wiederholungsaufgaben
# 05 - numpy
vector = np.array([[[[0]]],[[[1]]],[[[2]]],[[[3]]]])
print("vector:",vector)
print("vector.ravel:",vector.ravel())
print("vector.squeeze:",vector.squeeze())
print("vector.flatten:",vector.flatten())
print("vector.reshape(-1):",vector.reshape(-1))

vectorPy = [[[[0]]],[[[1]]],[[[2]]],[[[3]]]]
print("vectorPy:",vectorPy)
print("vectorPy.ravel:",vectorPy.ravel())
print("vectorPy.squeeze:",vectorPy.squeeze())
print("vectorPy.flatten:",vectorPy.flatten())
print("vectorPy.reshape(-1):",vectorPy.reshape(-1))
