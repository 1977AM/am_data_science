"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        dn_number: нижняя граница поиска
        up_number: верхняя граница поиска

    Returns:
        int: Число попыток
        
        
    """

    count = 0
    dn_number = 1
    up_number = 101
    while True:
        count += 1
        predict_number = np.random.randint(dn_number, up_number) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
        if predict_number > number:
            up_number = predict_number
        elif predict_number < number:
            dn_number = predict_number
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список  для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == "__main__":
    # RUN
    score_game(random_predict)