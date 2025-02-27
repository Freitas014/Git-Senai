def multiplicaMatriz(mat1, mat2):
    tam = len(mat1)
    mat3 = [[0 for j in range(tam)] for i in range(tam)]
    for i in range(tam):
        for j in range(tam):
            mat3 [i] [j] = (mat1 [i] [j] * mat2 [i] [j])
        return mat3