#   Feito por Léo
#   20/08/2022
#   Lib feita por cálculo numérico

import numpy as np

def det(table):
    table_np = np.array(table)

    n_lines = len(table_np)

    n_colum = len(table_np[0])

    if n_lines!=n_colum:
        print('This isn\'t a NxN matrix but we will adapt :)')

    for i in range(n_lines):
        if table_np[i][i] != 0:
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


def gauss(table):
    table_np = np.array(table)

    n_lines = len(table_np)

    n_colum = len(table_np[0])

    if n_lines+1!=n_colum:
        exit("We can't solve this... Please make sure this is right.")

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
            
    print(table_np)

    #implementação da parte que pegar as raizes.

    next_roots = list()
    
    for i in range(n_lines):
        soma = 0
        root = 0
        for j in range(i):
            soma += next_roots[j]*table_np[n_lines-1-i][n_colum-2-j]

        if table_np[n_lines-1-i][n_lines-1-i]:
            root =  (table_np[n_lines-1-i][n_colum-1] - soma)/table_np[n_lines-1-i][n_lines-1-i]

        next_roots.append(root)

    next_roots.reverse()

    return next_roots
