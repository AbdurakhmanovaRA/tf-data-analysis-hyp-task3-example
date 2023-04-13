import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 241769496 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p_value = stats.permutation_test(x, y,
                           method='exact',
                           func=lambda x, y: np.corrcoef(x, y)[1][0],
                           seed=0)
    return p_value >= 0.7 # Ваш ответ, True или False
