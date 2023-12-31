# Задание 2
# Напишите программу, которая бы выполняла следующие задачи:
# 1.	выводила название программы "Общество в начале XXI века";
# 2.	запрашивала у пользователя его возраст;
# 3.	если пользователь вводит числа от 0 до 7, то программа выводила надпись "Вам в детский сад";
# 4.	от 7 до 18 - "Вам в школу";
# 5.	от 18 до 25 - "Вам в профессиональное учебное заведение";
# 6.	от 25 до 60 - "Вам на работу";
# 7.	от 60 до 120 – "Вам предоставляется выбор";
# 8.	меньше 0 и больше 120 – пятикратный вывод надписи "Ошибка! Это программа для людей!"
# В программе желательно использовать все "атрибуты" структурного программирования:ветвление и цикл.

print('Общество в начале XXI века')
while True:
    while True:
        try:
            age = int(input('Enter your age: '))
            break
        except Exception as e:
            error_type = type(e).__name__
            print(f"Error accured: {error_type}")

    if 0 <= age < 7:
        print('Вам в детский сад')
    elif 7 <= age < 18:
        print('Вам в школу')
    elif 18 <= age < 25:
        print('Вам в профессиональное учебное заведение')
    elif 25 <= age < 60:
        print('Вам на работу')
    elif 60 <= age < 120:
        print('Вам предоставляется выбор')
    else:
        for i in range(5):
            print('Ошибка! Это программа для людей!')

    print('---------------------------------')
