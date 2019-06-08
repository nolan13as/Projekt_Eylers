### Задача 6 ###

a=0
b=0
for i in range(1,100,1):
    a+=i
    b+=(i*i)
a*=a
otvet=a-b
print(otvet)
