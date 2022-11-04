print('Задание 1\n')
# Написать калькулятор для простых операций(+,-,*,/,**), Операнды и оператор
# вводятся с клавиатуры отдельно(отдельные переменные)

list_of_operators = '''
Сложить два значения: нажмите +
Вычесть из первого значения второе: нажмите -
Умножить значения: нажмите *
Разделить первое значение на второе: нажмите /
Возвести певое значение в степень второго: нажмите **
'''
print('Онлайн калькулятор "Super Counter"', end='\n\n')

operand_1 = int(input('Введите первое значение: '))
print('\n')

print('Выберите операцию:', end='\n')
operator = (input(list_of_operators))
print('\n')

operand_2 = int(input('Введите второе значение: '))
print('\n')

if operator == '+':
    result = operand_1 + operand_2
elif operator == '-':
    result = operand_1 - operand_2
elif operator == '*':
    result = operand_1 * operand_2
elif operator == '/':
    result = operand_1 / operand_2
elif operator == '**':
    result = operand_1 ** operand_2
else:
    result = 'Вы ввели недопустимые символы и сломали "Super Counter" :( \nПовторите попытку.'

print('Результат:', result)
