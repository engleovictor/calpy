## Criado Por Léo
## 19/08/22
## Mod 28/08/22
## Mod 13/09/22
## Lib Feita pra Calculo Numérico

def bisection(f,x0=1e-5,x1=1e5,tol=1e-16,iterations=1000):
    for i in range(iterations+1):
        x = (x1+x0)/2
        var  = f(x)
        if var*f(x0) < 0:
            x1 = x
        elif var*f(x1) < 0:
            x0 = x
        elif var == 0 or abs(x1-x0) < tol:
            break
    return[x,i,abs(x1-x0)]

def fakeposition(f,x0=1e-5,x1=1e5,tol=1e-16,iterations=1000):    
    for i in range(iterations+1):
        err = max(abs(x1*f(x0)/(f(x0)-f(x1))), abs(x0*f(x1)/(f(x0)-f(x1))))
        x = (x1*abs(f(x0))+x0*abs(f(x1)))/(abs(f(x0))+abs(f(x1)))
        flv = f(x)
        if flv*f(x0) < 0:
            x1 = x
        elif flv*f(x1) < 0:
            x0 = x
        elif f(x) == 0 or abs(x1-x0) < tol:
            break
    return [x,i,err]
    
def fixedpoint(f,x0=None,tol=1e-16,iterations=1000):
    if x0 == None:
        exit('Preciso de um valor inicial')
    x = x0
    for i in range(iterations+1):
        flv = f(x)
        if flv == x or abs(flv - x) < tol:
            break
        x = flv
    return [x,i,abs(flv-x)]

def newtonraphson(f,df=None,x0=None,tol=1e-16,iterations=1000):
    if x0 == None:
        exit('Precisamos de um valor de x0')
    x = x0
    if df == None:
        df = lambda x: (f(x+1e-10)-f(x))/1e-10
    elif type(df) == "<class 'function'>":
        exit('Preciso de uma função derivada válida!!')
    for i in range(1,iterations+1):
        if f(x) == 0.0:
            return [x,i,0.]
        var = x
        x = x - f(x)/df(x)
        err = abs(x-var)
    return [x,i,err]

def secant(f,x0=1e-5,x1=1e5,tol=1e-16,iterations=1000):
    for i in range(iterations+1):
        if f(x1) == 0.0 or abs(x1-x0) < tol:
            break
        var = x1
        x1 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0 = var
    return [x1,i,abs(x1-x0)]
