import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 468441161 # Ваш chat ID, не меняйте название переменной

def solution(control_npv, test_npv) -> bool: 

    alpha = 0.03
    stat, p_value = ttest_ind(test_npv, control_npv, equal_var=False)

    return p_value < alpha
