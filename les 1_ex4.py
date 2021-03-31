n = int(input('Введите целое положительное число: '))

number = 0
max  = 0

while n%10 > max:
        max = n%10
        n = n//10
print (max)