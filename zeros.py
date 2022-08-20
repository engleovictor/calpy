#   Feito por Léo
#   19/08/2022
#   lib feita para calculo numerico

m = abs

def secant(f, x1=-1e3, x0=1e3,min_value = 1e-8, max_num_iter=10000):
    i = 0 
    c1 = x1
    c0 = x0
    for i in range(max_num_iter):
        var = c1
        c1 = c1 - f(c1)*(c1-c0)/(f(c1)-f(c0))
        c0 = var

        if abs(f(c1)) < min_value:
            break

    return [c1,i]

def bissec(f, a=-1e5, b=1e5, min_value = 1e-8, max_num_iter=10000):
    i = 0 
    
    for i in range(max_num_iter):
        c = (a+b)/2
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

        if abs(f(c)) < min_value:
            break

    return [c,i]

def falpos(f, a=-1e5, b=1e5, min_value = 1e-8, max_num_iter=10000):
    i = 0

    for i in range(max_num_iter):
        c = (m(f(b))*a - m(f(a))*b)/(f(b)-f(a))
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

        if abs(f(c)) < min_value:
            break

    return [c,i]

def mpfixo(f, cfv=0, min_value = 1e-8, max_num_iter=10000):
    i = 0
    c = cfv

    for i in range(max_num_iter):
        c = f(c)

        if abs(f(c)) < min_value:
            break

    return [c,i]

def newrap(f, cfv=0,min_value = 1e-8, max_num_iter=10000):
    df = lambda x: (f(x+1e-8)-f(x))/1e-8
    i = 0
    c = cfv
    for i in range(max_num_iter):
        c -= f(c)/df(c)

        if abs(f(c)) < min_value:
            break

    return [c,i]
