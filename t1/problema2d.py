import math
import scipy.special as spc
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')


#integrador numerico, con trapecio
def integrate(f, a, b, n=1000):
    value = (b-a)/n*(f(a)/2+f(b)/2)
    for k in range(1,n):
        value += 1.0*(b-a)/n*f(a+k*(b-a)/n)
    return value

#test integrador
#print math.sin(0.3)
#print integrate(math.cos,0,0.3)

#datos, x=18
x=18

#f_xr(x|r) es la distribucion de x dado r (p(x|r))
#coincide tambien con p(x,y), dado que p(r)=1
def f_xr(x,r):
    return spc.binom(33)*(1-r)**(33-x)*r**x

#r1r-> r^x * (1-r) ^(1-x)
def r1r(r):
    return 1.0*r**x * (1-r)**(33-x)
integral = integrate(r1r,0.0,1.0)

#p_rx(r) es la distribucion de r dado x (p(r|x))
def p_rx(r):
    return r1r(r)/integral

def r_less5():
    return integrate(p_rx,0.0,0.5)
def r_more5():
    return integrate(p_rx,0.5,1.0)

print('('+str(r_less5())+','+str(r_more5())+')')
