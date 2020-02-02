def div(n):
    if n < 1 or n > 1000 or int(n) != n: return 'Не натуральное число от 1 до 1000'
    # проверка простое ли число
    k = 0
    for i in range (2, n-1):
        if n%i == 0: k = k +1
    if k == 0: return 'Простое число'

    # все делители числа
    deliteli = []
    for i in range(1,n):
        if n%i == 0: deliteli.append(i)

    # Самый большой делитель
    max_del = 1
    for j in range(len(deliteli)):
        if div(deliteli[j]) == 'Простое число': max_del = deliteli[j]

    # print('Делители данного числа: ', deliteli)
    # print('Самый большой простой делитель: ', max_del)
    return 'Делители данного числа: ',deliteli, 'Самый большой простой делитель: ', max_del
