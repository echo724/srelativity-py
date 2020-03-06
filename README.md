# srelativity-py

A Python Module for special relativity mathematics. **srelativity-py** is using the symbolic math library **[sympy](https://www.sympy.org/en/index.html)**.

srelativity-py is made for calculating events by Lorentz Transformations used in Special Relativity. Using srelativity-py will help for getting a value of Lorentz factor, calculating event in moving frame, and dot product with two events in the Minkowski space.

## Dependencies

The following dependencies are required

- [sympy](https://www.sympy.org/en/index.html)

## Download

    $ git clone https://github.com/eunchan1001/srelativity-py.git

## Example

    from srelativity import *
    
    foo = LT(0.6) # makes Lorentz Transformation object with velocity 0.6(c)
    
    foo.rest(1,2) # makes event in rest frame (x,ct) coordinate
    foo.moving() # returns the coordinate of moving frame (x',ct')
    
    foo.gamma() # returns Lorentz factor 𝜸
    
    event2 = vec(2,1) # makes vector (2,1)
    foo.dot(event2) # returns dot product with Minkowski metric
    
    foo.inv() # returns inverse event coordinate
    
    foo.lt() # returns Lorentz Transformation sympy matrix (Map)

