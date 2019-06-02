### Задача 2 ###

last=0
Fiba=[1,2]
Summa=[]
a=0

while last<=4000000:
    last=Fiba[-1]+Fiba[-2]
    Fiba.append(last)
    print(Fiba)

Fiba.pop()
print(Fiba)

for i in Fiba:
    if i%2==0:
        Summa.append(i)
        print(Summa)

for i in Summa:
    a+=i
    print(a)
