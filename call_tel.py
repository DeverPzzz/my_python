#!/usr/bin/env python
# coding: utf-8

# In[35]:


#Упржнение 2.5 (call_tel.py)

x = int(input("Введите код города:\n"))
y = int(input("Введите к-во минут разговора:\n"))

if x == 343:
    print ('Ваша стоимость телефонных разговоров по Екатеринбургу:', y * 15, 'руб.')
elif x == 381:
    print ('Ваша стоимость телефонных разговоров по Омску:', y * 18, 'руб.')
elif x == 473:
    print ('Ваша стоимость телефонных разговоров по Воронежу:', y * 13, 'руб.')
elif x == 485:
    print ('Ваша стоимость телефонных разговоров по Ярославлю:', y * 11, 'руб.')
else:
    print ('Города нет в базе')