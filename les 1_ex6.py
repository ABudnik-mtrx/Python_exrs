a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))

number = 0

while a <= b:
    a = a*0.1 + a
    number +=1


print ('Номер дня: ', number+1)
