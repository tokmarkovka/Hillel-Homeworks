print('Задание 4*\n')
# Создайте приложение подбирающее правильное окончание к фразе: "Маша нашла
# в лесу {К} гриб...". K пользователь вводит с клавиатуры.
# Например: Маша нашла в лесу 7 грибОВ.
# Маша нашла в лесу 32 грибА.


# Составим список окончаний в зависимости от последней цифры в количестве грибов:

list_of_endings = '''
1 - пусто
2 - а
3 - а
4 - а
5 - ов
6 - ов
7 - ов
8 - ов
9 - ов
0 - ов
'''

mushrooms = int(input('Привет, Машенька! Напиши, сколько грибов собрала в лесу:'))
ending_of_word = str()

# если число грибов однозначное, задаем для каждого значения окончание

if mushrooms < 10:
    if mushrooms == 1:
        ending_of_word = ' '
    elif mushrooms == 2 or mushrooms == 2 or mushrooms == 3 or mushrooms == 4:
        ending_of_word = 'а'
    elif mushrooms == 5 or mushrooms == 6 or mushrooms == 7 or mushrooms == 8 or mushrooms == 9 or mushrooms == 0:
        ending_of_word = 'ов'

# есть исключения, значения с окончанием в промежутке между 10 и 20 имели бы все окончания "ов"
# поэтому выносим их в отдельное правило (для примера написала одно исключения, если Маша собрала не больше 100 грибов.
# к сожалению, крутила-вертела, но не получилось написать одно правило для всех окончаний.
# думала делить нацело на 10 и еще раз на 10 с остатком,
# чтобы если получаемая цифра-остаток равна 1 - то все окончания "ов", но работать такой код не захотел (


if 20 > mushrooms > 10:
    ending_of_word = 'ов'

# если число двухзначное, за исключением 11-19, прописываем такие правила для последней цифры:

if mushrooms > 20:
    last_number = mushrooms % 10
    if last_number == 1:
        ending_of_word = ' '
    elif last_number == 2 or last_number == 2 or last_number == 3 or last_number == 4:
        ending_of_word = 'а'
    elif last_number == 5 or last_number == 6 or last_number == 7 or last_number == 8 \
            or last_number == 9 or last_number == 0:
        ending_of_word = 'ов'

print(f'Поздравляем, ты собрала {mushrooms} гриб{ending_of_word}!')
