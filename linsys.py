## Feito por Léo
## 20/08/22 Mod 29/08/22
## Lib feita para Calculo Numérico

def GaussElimination(A):
    import numpy as np
    A = np.array(A)

    nl = len(A) 

    nc = len(A[0])

    if nl>nc:
        exit("Nao posso resolver isso....")

    for i in range(nl):
        if A[i][i] !=0:
            pivot = A[i][i]
        else:
            for j in range(i+1,nl):
                if A[j][i]:
                    ans = list(A[i])
                    A[i] = -A[j]
                    A[j] = np.array(ans)
                    pivot = A[i][i]
                    break

        for j in range(i+1,nl):
            if not A[j][i]:
                continue
            else:
                A[j] = A[j]*pivot - A[j][i]*A[i]
            
    if A[nl-1][nl-1] == 0:
        if A[nl-1][nc-1] == 0:
            exit('Esse sistema possui raizes indeterminadas!!')

        else:
            exit('Esse sistema não possui raizes!!')
    
    #implementação da parte que pegar as raizes.

    nr = list()
    
    for i in range(nl):
        sm = 0
        rt = 0
        for j in range(i):
            sm += nr[j]*A[nl-1-i][nc-2-j]

        if A[nl-1-i][nl-1-i]:
            rt =  (A[nl-1-i][nc-1] - sm)/A[nl-1-i][nl-1-i]

        nr.append(rt)

    nr.reverse()

    return nr

def LUdecomposition(A):
    import numpy as np
    
    A = np.array(A) 
    nl = np.shape(A)[0]
    L = np.eye(nl)
    
    for k in np.arange(nl):
        L[k+1:nl,k] = A[k+1:nl,k]/A[k,k]        
        for l in np.arange(k+1,nl):
            A[l,:] = A[l,:] - np.dot((L[l,k]),A[k,:])
        
    U = A
    
    return [L, U]


def gaussjacobi(A,b,x0,kmax):
    import numpy as np
    for i,line in enumerate(A):
        b[i] /= line[i]
        line /= line[i]
    M = A - np.eye(len(A))
    print(M)
    print(b)
    for i in range(kmax):
        x0 = b - M@x0
        if np.linalg.norm(x0) < 1e-3:
            break
    return [x0,kmax]



