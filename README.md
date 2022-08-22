# CALPY
## About
Lib for numerical calculation

## How to use?
First, download the lib:

    $ git clone https://github.com/engleovictor/calpy

Then, in the same directory:

    from calpy import *

### Zeros
Helps us to find equations roots.
#### Example 
    from calpy import zeros

    f = lambda x: x**3 - 4x

    x, i = zeros.bissec(f,a=0,b=6)

    print(f'{x} -- {i} iteractions')

    # x is the value
    # i number of iterations (has a max value).

### Linsys
Helps us to calculate determinants and solve equations(soon)
#### Example
    from calpy import linsys

    table1 = [
        [1,2],
        [5,7]
    ]

    print(linsys.det(table1))

    #it will print '-3'