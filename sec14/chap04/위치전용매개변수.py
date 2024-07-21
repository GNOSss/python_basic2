# 특정 매개변수들을 위치 전용으로 한정합니다.

def my_func(a, b, /, c, d): # 💡 / 이전의 매개변수는 위치로만
    print(a, b, c, d)

my_func(1, 2, d=4, c=3)
# my_func(a=1, b=2, c=3, d=4) # ⚠️ 에러 발생