"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number) -> int:
    """Компьютер угадывает число за минимальное кол. попыток.

    Args:
        number (int): Загаданное число.

    Returns:
        int: Число попыток
    """
    
    predict_number = np.random.randint(1, 101) # Загадываем рандомное число, используя генератор рандомных чисел
    count = 0 
    min = 1 
    max = 100
    
    while True:
        count += 1
        
        if predict_number > number:
            max = predict_number - 1
            predict_number = (max + min) // 2
        
        elif predict_number < number:
            min = predict_number + 1
            predict_number = (max + min) // 2
        
        else:
            break # Конец алгоритма и выход из цикла
    
    return(count)


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")


if __name__ == "__main__":
    # RUN
    score_game(random_predict)