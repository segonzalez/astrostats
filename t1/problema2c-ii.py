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

xpoint = np.arange(0,1,0.001)
ypoint = p_rx(xpoint)

xmaxv = np.argmax(ypoint)*0.001
ymaxv = np.amax(ypoint)
print('maximum at:' + '(' + str(xmaxv) + ',' + str(ymaxv) + ')')


##Plot routine for 
plt.plot(xpoint,ypoint,label='PDF')
#plt.axvline(x=xmaxv, ymin=0, ymax = ymaxv, linewidth=2,label=r'$'+str(xmaxv)+'$')
plt.scatter(np.array([xmaxv]),np.array([ymaxv]))
plt.annotate(r'$(' + str(np.round(xmaxv,2)) + ',' + str(np.round(ymaxv,2)) + ')$',(xmaxv+0.02,ymaxv+0.02))
plt.legend(loc=3)
plt.axis([0, 1, -0.1, 5])
plt.ylabel(r'$p(r|x)$')
plt.xlabel(r'$r$')
plt.savefig('PDF.pdf', bbox_inches='tight')
plt.show()

