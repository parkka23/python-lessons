# 2.	Написать программу поиска самого длинного
# слова в строке, разделенной точкой запятой.

string_=str(input('Enter string: '))
list_=string_.split(';')
list_ = [word.strip() for word in list_]
print(list_)
longest_word = max(list_, key = len)
position=string_.index(longest_word)
print('Longest word:',longest_word)
print('Position:',position)