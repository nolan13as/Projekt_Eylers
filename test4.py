### Задание 4 ###

<<<<<<< HEAD
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
=======
num=0                                   ### Пустая ячейка для записи данных
Sps=[]                                  ### пустой список
NumMax=0                                ### Тоже пустая ячейка
p="Это самое большое число Палидром"    ###
n="Это самое большое число Палидром!!!" ###
for i  in range(100,999,1) :            ### эти две строки для множителей
    for k in range(100,999,1):          ###
        num=i*k                         ### произведение
        nam=str(num)                    ### перерасчет int в str
        Sps=list(nam)                   ### запись этого числа в список каждым элементом
        if Sps[0]==Sps[-1] and Sps[1]==Sps[-2] and Sps[2]==Sps[-3]: ### проверка элементов
            if NumMax<num:              ### запись большего числа
                NumMax=num              ###
                print(NumMax)           ### принт большего числа
                print(p)                ###
>>>>>>> 4a8bb7663f71419d90587e5c6629c781e391e569
