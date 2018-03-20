import numpy
import np
"""
a = np.array([1,0,0,2,0,0,1])
p = np.poly1d(a)
#print(type(p))
b = np.array([1,0,0,0,0,0,0,-1])
q = np.poly1d(b)
#print(q/p)
f = q/p
print(f[1])
#c = np.array([13,0,0,13,13])
#g = np.poly1d(c)
print(f[1]+[13,0,0,13,13])

a1 = np.array([13,1])
p1 = np.poly1d(a1)
b1 = np.array([11])
q1 = np.poly1d(b1)
f = p1/q1
r = np.roots(p1/q1)
print(r)


a = [[13,-11],[13,13]]
a = np.array(a)
#print(a)
b = [-1,0]
b = np.array(b)
x = np.linalg.solve(a,b)
print(x)


a1 = np.array([2,3,1,12,4,1])
a = np.poly1d(a1)

b1 = np.array([1,0,0,2,0,0,1]) #x^6+2x^3+1
b = np.poly1d(b1)

c1 = np.array([2,3,1,3,10])
c = np.poly1d(c1)

d1 = np.array([1,0,0,0,0,0,0,-1]) #x^7-1
d = np.poly1d(d1)

print(a*b-c*d)

e1 = np.array([4,4,2,1])
e = np.poly1d(e1)

f1 = np.array([4,0,3,1,2,0])
f = np.poly1d(f1)

g1 = np.array([1,0,1,0,0,1])
g = np.poly1d(g1)

print(e*d-f*g)

aa1 = np.array([1,0,1,0,0,1])
aa = np.poly1d(aa1)"""


class op():
    def multiply(x,y):
        return x*y
    def division(x,y):
        return x/y
    def add(x,y):
        return x+y
    def subtraction(x,y):
        return x-y

    def calculation(x7, x6, x5, x4, x3, x2, x1, x0):
        f = np.array([x7, x6, x5, x4, x3, x2, x1, x0])
        f_x = np.poly1d(f)
        return f_x
"""
a = op.calculation(0,0,0,0,18,6,0,1)
b = op.calculation(0,0,0,0,0,0,1,2) #x+2
g = op.calculation(0,0,0,2,3,1,3,10)
c = op.calculation(0,0,0,18,6,0,4,1)
d = op.calculation(1,0,0,0,0,0,0,-1) #x^7
e = op.calculation(0,0,2,3,1,12,4,11)
f = op.calculation(0,1,0,0,2,0,0,1)



print(a+b*g)
print(c+b*e)

aa = op.calculation(0,0,0,0,0,0,0,1) #1
bb = op.calculation(0,0,0,0,0,1,2,0) #(x*x+2x)
cc = op.calculation(0,0,0,0,0,1,0,4) #x*x+4
dd = op.calculation(0,0,0,0,0,0,4,4) #4x+4
ee = op.calculation(0,0,0,1,2,4,8,1) #x^4+2x^3+...
ff = op.calculation(0,0,1,0,1,0,0,2) #x^5+x^3+2

print(op.multiply(aa+bb*dd,d)-op.multiply(cc+dd*ee,ff))
print()
print(aa+bb*dd,'\n')
print(op.multiply(cc+dd*ee,ff))
print('............................')

a1 = op.calculation(0,1,0,0,2,0,0,1)
b1 = op.calculation(0,2,7,12,7,2,10,10)
print(a1*b1)

a = op.calculation(0,0,0,0,4,3,0,1)
b = op.calculation(0,0,0,0,0,0,1,3) #x+3
d = op.calculation(1,0,0,0,0,0,0,-1) #x^7
c = op.calculation(0,0,0,3,2,4,2,4)
e = op.calculation(0,0,0,4,3,0,3,4)
f = op.calculation(0,0,3,2,4,1,0,2)
g = op.calculation(0,1,0,0,2,0,0,1)

print(op.multiply(d,a+b*c)-op.multiply(e+b*f,g))
print('\n')
print(a+b*c,'\n')
print(e+b*f)"""

a = op.calculation(0,3,4,5,4,3,2,2)
b = op.calculation(0,-1,1,-2,-1,-1,-2,-1)
print(a*b)