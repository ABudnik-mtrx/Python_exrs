time = int(input('Введите время в секундах: '))
hours = (time//3600)%24
min = (time//60)%60
sec = time%60

print (hours//10, hours%1,':',min//10, min%1, ':', sec//10, sec%1)
