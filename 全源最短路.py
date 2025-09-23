def floyd(mat: list) -> None: # 全源最短路
    n = len(mat)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if mat[i][j] > mat[i][k] + mat[k][j]:
                    mat[i][j] = mat[i][k] + mat[k][j]