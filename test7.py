### Задача 7 ###

otvet=0
count=1
for i in range(1,1000000,1):
    for k in range(2,i-1,1):
        if count==10001:
            break
        elif i%k==0 and i!=1:
            count+=1
            otvet+=i
print(otvet)
