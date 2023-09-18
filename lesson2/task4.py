# 4.	Написать программу которое находит
# введенное слово в строке которое также вводится
# пользователем в интерактивном режиме

string_=str(input('Enter string: '))
word=str(input('Enter word: '))

position=string_.index(word)
print('Position:',position)

