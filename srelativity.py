import sympy as sy

#class for Lorentz Transformation
#init with velocity(without c)
class LT:
    def __init__(self,v):
        self.__v = v
        self.__r = float(pow(1-pow(self.__v,2),-1/2))
        self.__lt = self.lt_setter()

#Setters
    def rest(self,x,y):
        self.__event = event(x,y)

    def lt_setter(self):
        row = 2
        col = 2
        M = [[0 for i in range(col)] for j in range(row)]
        M[0][0] = float(self.__r)
        M[0][1] = float(-self.__v*self.__r)
        M[1][0] = float(-self.__v*self.__r)
        M[1][1] = float(self.__r)
        return sy.Matrix(M)

#Getters
    def dot(self,mat):
        return self.__event.T*mink_dot()*mat

    def moving(self):
        return self.__lt*self.__event

    def gamma(self):
        return self.__r

    def inv(self):
        return self.__lt.inv()*self.__event

    def lt(self):
        return self.__lt

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
