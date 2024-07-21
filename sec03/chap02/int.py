int_1 = 123
int_2 = 123456789
int_3 = 123_456_789 # 긴 숫자를 가독성 좋게 표현 (_의 위치 무관)

int_1_type = type(int_1)
int_2_type = type(int_2)
int_3_type = type(int_3)

int_bin = 0b10101   # 2진법
int_oct = 0o777     # 8진법
int_hex = 0xA5F     # 16진법

# 💡 type의 결과를 str로 감싸면 Special Variables 펼치지 않고도 바로 표시
# print 시에는 필요 없음
int_bin_type = str(type(int_bin))
int_oct_type = str(type(int_oct))
int_hex_type = str(type(int_hex))

int_plus = 123 + int_bin + int_hex # 상호간 계산 가능

num = 5

num += 3 # 🛑 여기부터 브레이크포인트

num -= 4

num *= 8

num /= 4

num //= 1.5

num %= 3

num **= 3

pass
