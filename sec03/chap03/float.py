flt_1 = 3.14
flt_2 = 1.0
flt_3 = 123_456.789 # 역시 _ 사용 가능

flt_1_type = str(type(flt_1))
flt_2_type = str(type(flt_2))
flt_3_type = str(type(flt_3))

pass

import sys

# float 자료형의 바이트 수 출력
float_bytes = sys.getsizeof(float())
print("Float 자료형의 바이트 수:", float_bytes)

# float 자료형의 최대값과 최소값 출력
float_max = sys.float_info.max
float_min = sys.float_info.min
print("Float 자료형의 최대값:", float_max)
print("Float 자료형의 최소값:", float_min)
