### Задание 3 ###

for i in range(100851475143,1,-1):         # для каждого числа от 1 до 100851475143 (просто большое число , потому что логически больше он ни на какое число не поделится)
    if 600851475143%i==0:                  # если это число простое
        a=0                                # то в пустую ячейку
        a+=i                               # записать это число
        print(a)                           # вывести это число на экран
### Счет очень долгий последнее число было 716151937
