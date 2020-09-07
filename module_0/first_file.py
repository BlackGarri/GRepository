#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np


def game_score_my_ver(number, fpred=False):
    '''Алгоритм по модулю 0 для поиска загаданного числа с применением бинарного поиска.   
       Первоначальное число для сравнения с загаданным может определяется рандомным способом или устанавливаться
       по середине диапазона сравнения
    
    '''

    count = 1
    low, high = 1, 100
    
    if number != low and number != high:
        if fpred:
            predict = (low + high)//2  # вычисление среднего числа для определения диапазона сравнения
        else:
            predict = np.random.randint(1,101) # генерация случайного числа для определения диапазона сравнения

        while number != predict:
            count += 1
            if number > predict:
                low = predict + 1
            else:
                high = predict - 1
            predict = (low + high)//2
    
    return(count) 
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    
    '''
    
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
   
    return(score)


score_game(game_score_my_ver)

