import numpy.random as rd

numX = 0

for i in range(0,1000):
   num1=0
   num2=0
   for j in range(0,33):
      
      r = rd.rand()
      if(r < 0.5):
          num1+=1
      else:
          num2+=1
   if(num1==18):
      numX+=1
print(numX)
print(numX*1.0/1000)
