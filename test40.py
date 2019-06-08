### Задача 40 ###
a=[]
b=''
for i in range(1,200000,1):
    a.append(str(i))
for i in a:
    b+=i
a.clear()
a.append(int(b))
last=a.pop()
lust=str(last)
a=list(lust)
otvet=int(a[1])+int(a[10])+int(a[100])+int(a[1000])+int(a[10000])+int(a[100000])+int(a[1000000])
print(otvet)
