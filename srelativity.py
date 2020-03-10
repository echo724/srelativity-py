import sympy as sy

#class for Lorentz Transformation
#init with velocity(without c)
class LT:
    def __init__(self):
        self._c = 3 * pow(10,8)

    def v(self,v):
        self._v = v
        if self._v is not 1:
            self._r = float(pow(1-pow(self._v,2),-1/2))
            self._lt = self.lt_setter()
    def r(self,r):
        self._r = r
#Setters
    #Event at Rest frame
    def rest(self,x,y):
        self._event = event(x,y)
    #Lorentz transformation
    def lt_setter(self):
        row = 2
        col = 2
        M = [[0 for i in range(col)] for j in range(row)]
        M[0][0] = float(self._r)
        M[0][1] = float(-self._v*self._r)
        M[1][0] = float(-self._v*self._r)
        M[1][1] = float(self._r)
        return sy.Matrix(M)
    # Momentum
    def p(self):
        self._p = self._r*self._m*self._v
        return self._p

    #Total Energy
    def e(self):
        self._e = self._r*self._m
        return self._e

    #Kinetic Energy
    def ke(self):
        self._ke = (self._r - 1)*self._m
        return self._ke

    #Mass in Moving Frame
    def m(self,mass):
        self._m = mass
        return self._m

    def relation(self):
        sol = input("Which Solution(p,e,m): ")
        if sol is "p":
            p_square = pow(self._e,2) - pow(self._m,2)
            print("Squared: {0}".format(p_square))
            self._p = sy.sqrt(p_square)
            print("Momentum is {0}".format(self._p))

        if sol is "e":
            e_square = pow(self._m,2) + pow(self._p,2)
            print("Squared: {0}".format(e_square))
            self._e = sy.sqrt(e_square)
            print("Energy is {0}".format(self._e))

        if sol is "m":
            m_square = pow(self._e,2) - pow(self._p,2)
            print("Squared: {0}".format(m_square))
            self._m = sy.sqrt(m_square)
            print("Mass is {0}".format(self._m))
        else:
            print("Invaild Type")
#Getters
    #Dot product on Minkowhski space
    def dot(self,mat):
        return self._event.T*mink_dot()*mat
    #Event at moving frame
    def mov(self):
        return self._lt*self._event
    #Inverse Lorentz transformation
    def inv(self):
        return self._lt.inv()*self._event




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

def am(kg):
    u = 1.66 * pow(10,-27)
    return kg/u

def Mev(u):
    c_sq = 931.5
    return c_sq * u

def beta(gamma):
    return sy.sqrt(abs(1 - 1/pow(gamma,2)))
