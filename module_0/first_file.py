#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


def game_core_v1(number):
    '''Алгоритм авторов курса - версия 1
       Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток
    
    '''

    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict: 
            return(count) # выход из цикла, если угадали

        
def game_core_v2(number):
    '''Алгоритм авторов курса - версия 2
       Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    '''
    
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали

def game_score_my_ver(number):
    '''Алгоритм обучающегося по модулю 0
       Поиск загаданного числа с применением алгоритма бинарного поиска.   
       Первоначальное число для сравнения с загаданным определяется рандомным способом
    
    '''

    count = 1
    low_val = 1
    high_val = 100

    predict_val = np.random.randint(1,101) # генерация случайного числа для определения диапазона сравнения
                                           # можно использовать середину диапазона predict_val = 50
        
    while number != predict_val:
        count += 1
        if number > predict_val:
            low_val = predict_val + 1
        else:
            high_val = predict_val - 1
        predict_val = (low_val + high_val) // 2
    return(count) # выход из цикла, если угадали    
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    
    '''
    
    count_ls = []
    np.random.seed()  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_score_my_ver)

# score_game(game_core_v1)        # сравнение с алгоритмом 1, предложенным авторами курса

# score_game(game_core_v2)        # сравнение с алгоритмом 2, предложенным авторами курса




# In[ ]:




