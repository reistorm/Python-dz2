# Задайте список из n чисел последовательности 
# (1 + 1/n)^n и выведите на экран их сумму.

def sq_number(n):
    
    if n == 0:
        print('N не равен 0')
        return 0
    for n in range(1, n+1):
        n = round(((1 + n) ** n / n ** n), 2)
        print(n, end=' ')

sq_number(8)