### Задача 9 ###
import math
a=0
a2=0
b=0
b2=0
c=0
c2=0
for i in range(1,999,1):
    for k in range(1,999,1):
        a2=i**2
        b2=k**2
        c2=a2+b2
        a=math.sqrt(a2)
        b=math.sqrt(b2)
        c=math.sqrt(c2)
        if a+b+c==1000:
            print(a)
            print(b)
            print(c)
