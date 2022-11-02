print('Задание *\n')
# Микропроцессор электронных часов считает количество секунд прошедших от
# начала суток (значение вводится с клавиатуры пользователем). Необходимо
# написать программу отображающую время в формате чч:мм:сс.
# Например: 9375 -> 2:36:15

a_lot_of_seconds = input('Введите количество секунд, прошедших от начала суток: ')
a_lot_of_seconds = int(a_lot_of_seconds)

# в одном часе 3600 секунд, считаем количество целых часов путем деления нацело:

hours = a_lot_of_seconds // 3600

# затем берем остаток от деления, чтобы не учитывать опять часы и переводим
# остаток секунд в минуты также путем деления нацело ( в одной минуте 60 секунд).
minutes = a_lot_of_seconds % 3600 // 60

# затем из введенного пользователем общего количество секунд вычитаем наши часы,
# переведенные в секунды и наши минуты, переведенные в секунды, получаем остаток
# секунд (тут тоже можно еще придумать еще несколько вариантов)
seconds = a_lot_of_seconds - (hours * 3600) - (minutes * 60)

print(f'Время в формате чч:мм:сс : {hours}:{minutes}:{seconds}')
