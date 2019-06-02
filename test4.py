### Задание 4 ###

num=0
Sps=[]

for i  in range(500,999,1) :
    for k in range(500,999,1):
        num=i*k
        nam=str(num)
        Sps=list(nam)
        if Sps[1]==Sps[-1] and Sps[2]==Sps[-2] and Sps[3]==Sps[-3]:
            print(num)
