name = input('Здравствуйте, как Ваше имя?: ')
print ('Добро пожаловать, ', name,'!')
age = int(input ('Сколько Вам лет?: '))
city = input ('В каком городе Вы живете?: ')
work_year = int(input ('Укажите год начала Вашей работы?: '))
income = int(input('Укажите уровень Вашего ежемесячного дохода: '))
work_age = 2021-work_year
work_age_perc = (work_age/age)*100
print ('Ваш стаж составляет', work_age, 'лет.\n')
print ('Вы потратили на работу', work_age_perc//1, 'процентов своего жизненного времени!' )