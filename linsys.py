#   Feito por Léo
#   20/08/2022
#   Lib feita por cálculo numérico

import numpy as np

def det(table):
    table_np = np.array(table)

    n_lines = len(table_np)

    n_colum = len(table_np[0])

    if n_lines!=n_colum:
        exit("error: linsys was expecting a NxN matrix.")

    for i in range(n_lines):
        if table_np[i][i] !=0:
            pivot = table_np[i][i]
        else:

            for j in range(i+1,n_lines):
                if table_np[j][i]:
                    ans = list(table_np[i])
                    
                    table_np[i] = -table_np[j]
                    
                    table_np[j] = np.array(ans)

                    pivot = table_np[i][i]

                    break

        for j in range(i+1,n_lines):
            if not table_np[j][i]:
                continue
            else:
                table_np[j] = table_np[j]*pivot - table_np[j][i]*table_np[i]

    return table_np[n_lines-1][n_lines-1]

