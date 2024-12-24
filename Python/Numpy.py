import numpy as np
import random as rd
def random2darray(r,c):
    array = np.array([[rd.randint(-10,10) for i in range(c)] for i in range(r)])
    return array
def random3dvector():
    vector = np.array([rd.randint(-10,10) for i in range(3)])
    return vector

v1 = random3dvector()
v2 = random3dvector()

print(f'Vector 1: \n{v1}')
print(f'Vector 2: \n{v2}')
print(f'vector 1 + vetor2: \n{v1 + v2}')
print(f'Vector 1 - Vector 2: \n{v1 - v2}')
print(f'Dot Product of Vector 1 and Vector 2: \n{np.dot(v1,v2)}')
print(f'Cross Product of Vector 1 and Vector 2: \n{np.cross(v1,v2)}')

m1 = random2darray(3,3)
m2 = random2darray(3,3)

print(f'Matrix 1: \n{m1}')
print(f'Matrix 2: \n{m2}')
print(f'Matrix 1 + Matrix 2: \n{m1 + m2}')
print(f'Matrix 1 - Matrix 2: \n{m1 - m2}')
print(f'Matrix 1 x Matrix 2: \n{np.dot(m1,m2)}')
print(f'Matrix 1 Transpose: \n{m1.T}')
print(f'8 * Matrix 1  Transpose: \n{8*m1}')






