## Criado Por Léo
## 19/08/22
## Mod 28/08/22
## Lib Feita pra Calculo Numérico

def bisection(f,x0=1e-5,x1=1e5,iterations=1000):
    x = (x1+x0)/2
    if f(x) == 0.0:
        return [x,1,0.]
    else:
        for i in range(2,iterations+1):
            var = f(x)
            
            if var*f(x0) < 0:
                x1 = x
            else:
                x0 = x

            x = (x1+x0)/2

            err = (x1-x0)/2
            
            if f(x) == 0.0:
                return [x,i,err]

        return [x,iterations,err]

def fakeposition(f,x0=1e-5,x1=1e5,iterations=1000):    
    x = (x1*abs(f(x0))+x0*abs(f(x1)))/(abs(f(x0))+abs(f(x1)))
    if f(x) == 0.0:
        return [x,1,0.]
    else:
        for i in range(2,iterations+1):
            var = f(x)
            
            if var*f(x0) < 0:
                x1 = x
            else:
                x0 = x

            x = (x1*abs(f(x0))+x0*abs(f(x1)))/(abs(f(x0))+abs(f(x1)))

            err = max(abs(x1*f(x0)/(f(x0)-f(x1))), abs(x0*f(x1)/(f(x0)-f(x1))))
            
            if f(x) == 0.0:
                return [x,i,0.]

        return [x,iterations,err]
    
def fixedpoint(f,x0=None,iterations=1000):
    if not x0:
        exit('Precisa do valor de x0!!')
    
    x = f(x0)

    if x == f(x):
        return [x,1,0.]
    else:
        for i in range(2,iterations+1):
            j = 0
            var = x
            x = f(x)
            err = abs(x - var)
            if x == f(x):
                return [x,i,0.]
            else:
                if abs(f(x)) - abs(f(var)) > 1:
                   j+=1
                   if j > 5:
                    exit('\nEscolha outra funcao de iteracao.\nEssa não converge!!')
                                
        return [x,iterations,err]
                

def newtonraphson(f,df=None,x0=None,iterations=1000):
    if not x0:
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

def secant(f,x0=1e-5,x1=1e5,iterations=1000):
    var = x1
    x1 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
    x0 = var
    if f(x1) == 0.0:
        return [x1,1,0.]
    else:
        for i in range(2,iterations+1):
            var = x1
            x1 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
            x0 = var

            err = x1 - x0

            if f(x1) == 0.0:
                return [x1,i,0.]

    return [x1,i,err]

