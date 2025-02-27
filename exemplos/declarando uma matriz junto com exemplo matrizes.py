def leMatriz(dimensao):
    mat = [[] for i in range(dimensao)]
    for i in range(dimensao):
        for j in range(dimensao):
            num = int(input("(" + str(i + 1) + "," + str(j + 1) + ") : "))
            mat[i].append(num)
        return mat

def imprimeMatriz(mat):
    for linha in mat:
        for numero in linha:
            print(numero, end=" ")
            #imprime números na mesma linha separados por espaço
        print() # após impressão de uma linha, pula uma linha

def somaMatriz(mat1, mat2):
    tam = len(mat1)
    mat3 = [[0 for j in range(tam)] for i in range(tam)]
    for i in range(tam):
        for j in range(tam):
            mat3[i] [j] = mat1[i] [j] + mat2 [i] [j]
        return mat3
    
def multiplicaMatriz(mat1, mat2):
    tam = len(mat1)
    mat3 = [[0 for j in range(tam)] for i in range(tam)]
    for i in range(tam):
        for j in range(tam):
            mat3 [i] [j] = (mat1 [i] [j] * mat2 [i] [j])
        return mat3
    
dimensao = int(input("Digite a dimensão da matriz: "))
mat = leMatriz(dimensao)
imprimeMatriz(mat)
n = int(input("Dimensão das matrizes: "))
mat1 = leMatriz(n)
mat2 = leMatriz(n)
print("mat1: ")
imprimeMatriz(mat1)
print("mat2: ")
mat3soma = somaMatriz(mat1, mat2)
print("Soma: ")
imprimeMatriz(mat3soma)
mat3Mult = multiplicaMatriz(mat1, mat2)
print("Multiplicação: ")
imprimeMatriz(mat3Mult)