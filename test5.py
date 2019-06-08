### Задача 5 ###

def maloe():
    coin= 0
    while coin <20:
        for i in range(500000,5000000,1):
            for k in range(1,20,1):
                if i%k==0:
                    coin+=1
                    yield i
                    print(coin)
                else :
                    coin=0
for i in maloe():
    print(i)
