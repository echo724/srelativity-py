import sympy as sy

#class for Lorentz Transformation
#init with velocity(without c)
class LT:
    def __init__(self,v):
        self._v = v
        self._r = float(pow(1-pow(self._v,2),-1/2))
        self._lt = self.lt_setter()

#Setters
    def rest(self,x,y):
        self._event = event(x,y)

    def lt_setter(self):
        row = 2
        col = 2
        M = [[0 for i in range(col)] for j in range(row)]
        M[0][0] = float(self._r)
        M[0][1] = float(-self._v*self._r)
        M[1][0] = float(-self._v*self._r)
        M[1][1] = float(self._r)
        return sy.Matrix(M)

#Getters
    def dot(self,mat):
        return self._event.T*mink_dot()*mat

    def moving(self):
        return self._lt*self._event

    def gamma(self):
        return self._r

    def inv(self):
        return self._lt.inv()*self._event

    def lt(self):
        return self._lt

#Functions used in special relativity calculations
def sl(r,l):
    return float(l/r)
def td(r,t):
    return float(r*t)

def rel_v(v1,v2):
    return (v1+v2)/(1+(v1*v2))

def mink_dot():
    row = 2
    col = 2
    M = [[0 for i in range(col)] for j in range(row)]
    M[0][0] = 1
    M[0][1] = 0
    M[1][0] = 0
    M[1][1] = -1
    return sy.Matrix(M)

def event(x,y):
    row = 1
    col = 2
    M = [0 for i in range(col)]
    M[0] = x
    M[1] = y
    return sy.Matrix(M)
