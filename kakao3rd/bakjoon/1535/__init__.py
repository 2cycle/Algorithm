#recursion

m=list()
def mat(i ,j):
    if i ==1 and j == 1:
        return m[i][j]
    elif i == 1:
        return mat[i, j-1] + m[i][j]
    elif j == 1:
        return mat[i-1, j] + m[i][j]
    else:
        return min(mat(i,j-1),mat(i-1,j)) + m[i][j]




# dp  bottom up
L = list() #dp
def matDP(i ,j):
    if L[i][j] != -1 : return L[i][j]
    elif i ==1 and j == 1:
        L[i][j] = mat(i, j-1) + m[i][j]
    elif i == 1:
        L[i][j] = mat[i, j - 1] + m[i][j]
    elif j == 1:
        L[i][j] = mat[i-1, j] + m[i][j]
    else:
        L[i][j] = min(mat(i,j-1),mat(i-1,j)) + m[i][j]
    return L[i][j]