### Задача 2 ###
last=0
Fiba=[1,2]

while last<=4000000:
    last=Fiba[-1]+Fiba[-2]
    Fiba.append(last)
    print(Fiba)
