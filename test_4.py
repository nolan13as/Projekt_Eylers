#тест четвертый#

num=0
Sps=[]
NumMax=0
p="Это самое большое число Палидром"
n="Это самое большое число Палидром!!!"
for i  in range(100,999,1) :
    for k in range(100,999,1):
        num=i*k
        nam=str(num)
        Sps=list(nam)
        if Sps[0]==Sps[-1] and Sps[1]==Sps[-2] and Sps[2]==Sps[-3]:
            if NumMax<num:
                NumMax=num
                print(NumMax)
                print(p)
