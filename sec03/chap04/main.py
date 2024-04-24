import sys

# 양수 무한대와 음수 무한대
inf_pos = float('inf')
inf_neg = float('-inf')

pos_neg = inf_pos == -inf_neg

# 무한대는 표현가능한 가장 큰 수보다 큼
inf_big_1 = inf_pos > sys.float_info.max
inf_big_2 = inf_neg < -sys.float_info.max

# 무한대에 값을 더하거나 빼도 무한대
inf_still_1 = inf_pos + 1 == inf_pos
inf_still_2 = inf_pos - 1 == inf_pos

nan_1 = float('nan')
nan_2 = float('nan')

nan_type = str(type(nan_1))

nan_are_same = nan_1 == nan_2

# 다른 숫자와의 산술연산은 nan 반환
nan_calc_1 = nan_1 + 1
nan_calc_2 = nan_1 / 2

# 다른 숫자와의 비교 연산은 False를 반환
nan_calc_3 = nan_1 > 0
nan_calc_4 = nan_1 < 0
nan_calc_5 = nan_1 < float('inf')

pass