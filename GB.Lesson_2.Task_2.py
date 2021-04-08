my_list = list(input('Введите значения: '))
print (my_list)

a = list(my_list[-1])


if len(my_list)%2 == 0:
    my_list[::2], my_list[1::2] = my_list[1::2],my_list[::2]
    print(my_list)
else:
    new_my_list = my_list[:-1]
    new_my_list[::2], new_my_list[1::2] = new_my_list[1::2], new_my_list[::2]
    q= new_my_list
    print (q+a)