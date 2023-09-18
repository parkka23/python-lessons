# 3.	Написать программу самого короткого слова
# который выделяется знаком который пользователь вводит
# в интерактивном режиме

string_=str(input('Enter string: '))
symbol=str(input('Enter symbol: '))

list_=string_.split()
print(list_)

valid_list=[word for word in list_ if symbol in word]
print(valid_list)

if valid_list:
    shortest_word = min(valid_list, key=len)
    position = string_.index(shortest_word)
    print('Shortest word:', shortest_word)
    print('Position:', position)
else:
    print('Word Not Found')


