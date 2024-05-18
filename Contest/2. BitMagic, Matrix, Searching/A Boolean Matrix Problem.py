def booleanMatrix(mat,m,n):
    #Your code here
    mod_row = set()
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                mod_row.add(i)
                break
            
    for k in mod_row:
        for j in range(n):
            mat[k][j] = 1
            
    return mat
