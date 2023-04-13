import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 241769496 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p_value = stats.permutation_test(x, y, statistic, vectorized=True,
                       n_resamples=np.inf, alternative='less')
    return p_value >= 0.7 # Ваш ответ, True или False
