# O objeto mais simples da biblioteca é o array que serve para criar vetores homogêneos multidimensionais.
# Um array pode ser criado a partir de uma lista:

import numpy as np
a = np.array([1,2,3])
print(a.ndim) #ndim -> número de dimensão
print(a.size) 
print(a)

# pra dar espaço entre um exemplo e outro
print()
print('-=' * 30)

import numpy as np
b = np.array([[1,2,3], [4,5,6]])
print(b.ndim)
print(b.size)
print(b)

print()
print('-=' * 30)

a = np.arange(10)
print(a)
a = np.arange(10).reshape(2,5)
print(a)

print()
print('-=' * 30)

a = np.zeros((3))
print(a)
a = np.zeros((3,4))
print(a)

print()
print('-=' * 30)

m = np.ones((2,3))
m = m + 1      
# m = m*4
#m = m**3
print(m)

print()
print('-=' * 30)

A = np.array([[1,1], [0,1]])
B = np.array([[2,0], [3,4]])
C = A*B
print(C)

print()
print('-=' * 30)



