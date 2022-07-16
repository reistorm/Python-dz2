# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sum_num(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0
num = input('Введите число: ')
a = int(sum_num(num))
b = float(num)
if a != 0:
    for i in range(a):
        b *= 10
b = int(b)
c = 0
for i in range(len(num) - 1):
    c += b % 10
    b //= 10
print("Сумма цифр числа:", c)




# Обшее решение:
# for digit in n:
#     if digit.isdigit():
#         suma += int(digit)
        
 
# print("Сумма:", suma)
