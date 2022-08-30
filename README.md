# CALPY
## About
Lib for numerical calculation

## How to use?
First, download the lib:

    $ git clone https://github.com/engleovictor/calpy

Then, in the same directory:

    from calpy import *
    #OR
    from calpy.zeros import *
    #OR
    from calpy.linsys import *


### Zeros
Helps us to find equations roots.
#### Example 
    from calpy import zeros
    import math as mt

    f = lambda x: x - mt.cos(x)

    x, i, err = zeros.bisection(f)

    print(f'{x} -- {i} iteractions')

    # x is the value
    # i number of iterations (has a max value).
    # err the error

### Linsys
Helps us to calculate determinants and solve equations(soon)
#### Example
    from calpy import linsys

    table1 = [
        [1,2],
        [5,7]
    ]

    print(linsys.determinant(table1))

    #it will print '-3'

    table2 = [
        [1,2,4],
        [5,7,8]
    ]

    print(linsys.GaussElimination(table2))
    