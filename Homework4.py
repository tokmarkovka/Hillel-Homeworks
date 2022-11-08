print('Задание 1\n')

# Напоминаю, использовать цикл в цикле. Решение с манипуляцией строк не засчитаю.
# Размер фигур вводится пользователем с клавиатуры.
# Рисунки в архиве.
'''
а.
*
* *
* * *
* *
*
б.
* * * * *
  * * *
    *
в.	
        *
	  * *
	* * *
	  * *
	    *
г.



    *
  * * *	
* * * * *
'''

# height = int(input('Введите высоту фигуры: '))
# weight = height
#
# for h in range(height, 0, -1):
#     for w in range(0, h):
#         print('*', end=' ')
#     print()
#
# height = int(input('Введите высоту фигуры: '))
# weight = height
#
# for h in range(0, height):
#     for i in range(h, height - 1):
#         print(' ', end=' ')
#     for w in range(0, h + 1):
#         print('*', end=' ')
#     print()
#  если пользователь вводит четное число, программа добавляет 1

height = int(input('Введите высоту фигуры: '))

if height % 2 == 0:
    height = height + 1

weight = height

print('- фигура "a":\n')

for h in range(height):
    for w in range(h + 1):
        print('*', end=" ")
    print()
for h in range(height, 0, -1):
    for w in range(h - 1):
        print('*', end=" ")
    print()

print('- фигура "б":\n')

weight = height * 2 - 1

for h in range(height):
    for w in range(weight):
        if w < h:
            print(' ', end=" ")
            continue
        if w + h >= weight:
            print(' ', end=" ")
            continue
        print('*', end=" ")
    print()

print('- фигура "в":\n')

weight = height

for h in range(height):
    for w in range(weight):
        if h + w >= weight:
            print('*', end=" ")
            continue
        print(' ', end=" ")
    print()
for h in range(height, 0, -1):
    for w in range(weight):
        if h + w >= weight:
            print('*', end=" ")
            continue
        print(' ', end=" ")
    print()

print('- фигура "г":\n')

weight = height * 2 - 1

for h in range(height):
    for w in range(weight):
        if h + w <= height - 2:
            print(' ', end=" ")
            continue
        if w - h <= height - 1:
            print('*', end=" ")
            continue
        print(' ', end=" ")
    print()
