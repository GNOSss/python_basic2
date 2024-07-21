# 개발자를 위한 경고 메시지를 발생시킵니다.
# 오류가 일어나지는 않지만 향후 문제의 소지가 있거나
# 올바르지 않게 코드가 작성된 경우를 위해 사용됩니다.

import warnings

def old_function():
    warnings.warn(
        "이 함수는 향후 버전에서 제거됩니다. new_function()을 사용하세요.",
        DeprecationWarning
    )
    print("이전 함수")


def new_function():
    print("새 함수")


# 함수 사용 예
old_function()
new_function()






import warnings


def input_positive(x):
    if x < 0:
        warnings.warn(f"{x}은(는) 음수입니다.", RuntimeWarning)
        return x


res_1 = input_positive(1)
res_2 = input_positive(-1)
