# 매개변수를 기억하는 내부함수

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)


mults = [(times3(i), times5(i)) for i in range(1, 10)]

pass