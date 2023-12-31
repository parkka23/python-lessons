# Задание 1
# Напишите код по следующему словесному алгоритму:
# 1.	Попросить пользователя ввести число от 1 до 9. Полученные данные связать с переменной x.
# 2.	Если пользователь ввел число от 1 до 3 включительно, то …
# ●	 попросить пользователя ввести строку. Полученные данные связать с переменной s;
# ●	 попросить пользователя ввести число повторов строки. Полученные данные связать с переменной n, предварительно преобразовав их в целочисленный тип;
# ●	 выполнить цикл повторения строки n раз;
# ●	 вывести результат работы цикла.
# 3.	Если пользователь ввел число от 4 до 6 включительно, то …
# ●	 попросить пользователя ввести степень, в которую следует возвести число. Полученные данные связать с переменной m;
# ●	 реализовать возведение числа x в степень m;
# ●	 вывести полученный результат.
# 4.	Если пользователь ввел число от 7 до 9, то выполнить увеличения числа x на единицу в цикле 10 раз, при этом на экран вывести все 10 чисел.
# 5.	Во всех остальных случаях выводить надпись "Ошибка ввода".

while True:
    try:
        x = float(input('Enter a number in the range of 1 to 9: '))
    except Exception as e:
        error_type = type(e).__name__
        print(f"Error accured: {error_type}")
    else:
        if 1 <= x <= 3:
            s = str(input('Enter a string: '))
            while True:
                try:
                    n = int(input('Enter a number of iterations: '))
                    break
                except Exception as e:
                    error_type = type(e).__name__
                    print(f"Error accured: {error_type}")
            for i in range(n):
                print(i + 1, '. ', s, sep='')

        elif 4 <= x <= 6:
            while True:
                try:
                    m = int(input('Enter an exponent: '))
                    break
                except Exception as e:
                    error_type = type(e).__name__
                    print(f"Error accured: {error_type}")
            print(x,'^',m,'=',x ** m)

        elif 7 <= x <= 9:
            for i in range(10):
                x += 1
                print(i + 1, '. ', x, sep='')

        else:
            print('Input Error')
        print('-----------------------------------------------------')
