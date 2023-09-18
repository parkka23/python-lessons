# 5.	Посчитать количество слов в предложении
# которое вводит пользователь

string_=str(input('Enter string: '))
list_=string_.split()
length=len(list_)
print('Number words:',length)