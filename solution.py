import pandas as pd
import numpy as np
from hyppo.ksample import MMD

chat_id = 415542660 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    ans = anderson_ksamp([x, y]) < 0.04
    return ans # Ваш ответ, True или False
