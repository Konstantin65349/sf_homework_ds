"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
import random

def random_predict(number) -> int:
    """Компьютер угадывает число за минимальное кол. попыток.

    Args:
        number (int): Загаданное число.

    Returns:
        int: Число попыток
    """
    random.seed(1) # фиксируем сид для воспроизводимости
    predict_number = np.random.randint(1, 101) # Загадываем рандомное число, используя генератор рандомных чисел
    count = 0 
    min_number = 1 
    max_number = 100
    
    while True:
        count += 1
        
        if count > 50: break
        
        if predict_number > number:
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2
        
        elif predict_number < number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2
        
        else:
            break # Конец алгоритма и выход из цикла
    
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    return score


if __name__ == "__main__":
    # RUN
    print(f"Ваш алгоритм угадывает число в среднем за:{score_game(random_predict)} попыток")