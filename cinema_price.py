#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Упржнение 2.6 (cinema_price.py)

#Условие скидки при покупке за 1 день
z = input("Сегодня/завтра: ")

if z == "Завтра":
    d1 =0.05
elif z== "Сегодня":
    d1 = 0
else:
    print("Нет сеансов")

#Условие скидки при покупке для компании 20+ человек
n = int(input("К-во билетов: "))

if n >= 20:
    d2 = 0.2
elif 1 <= n < 20:
    d2 = 0
else:
    print ("Как это?")

#Расчет стоимости
x = input("Фильм: ")

if x == 'Пятница':
    y = int(input("Время сеанса:"))
    if y == 12:
        print('Стоимость билетов:', (250 - 250*d1 - 250*d2)*n, 'руб.')
    elif y == 16:
        print('Стоимость билетов:', (350 - 350*d1 - 350*d2)*n, 'руб.')
    elif y == 20:
        print('Стоимость билетов:', (450 - 450*d1 - 450*d2)*n, 'руб.')
    else:
        print('Нет такого времени для этого фильма')
        
elif x == 'Чемпионы':
    y = int(input("Время сеанса:"))
    if y == 10:
        print('Стоимость билетов:', (250 - 250*d1 - 250*d2)*n, 'руб.')
    elif y == 13:
        print('Стоимость билетов:', (350 - 350*d1 - 350*d2)*n, 'руб.')
    elif y == 16:
        print('Стоимость билетов:', (350 - 350*d1 - 350*d2)*n, 'руб.')
    else:
        print('Нет такого времени для этого фильма')
        
elif x == 'Пернатая банда':
    y = int(input("Время сеанса: "))
    if y == 10:
        print('Стоимость билетов:', (350 - 350*d1 - 350*d2)*n, 'руб.')
    elif y == 14:
        print('Стоимость билетов:', (450 - 450*d1 - 450*d2)*n, 'руб.')
    elif y == 18:
        print('Стоимость билетов:', (450 - 450*d1 - 450*d2)*n, 'руб.')
    else:
        print('Нет такого времени для этого фильма')
        
else:
    print('Нет такого фильма в прокате')