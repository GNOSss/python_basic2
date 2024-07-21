# ascii()
# 객체를 ASCII 문자열로 변환하며, 비ASCII 문자는 이스케이프 시퀀스로 표현
ascii_text_1 = ascii("Hello")
ascii_text_2 = ascii("안녕하세요")


# bytearray()
# 변경 가능한 바이트 배열을 생성
# 0~255 사이의 정수만 담음. 바이너리 데이터 등에 사용
ba = bytearray([50, 100, 76, 72, 90])
ba_1 = ba[1]

# 그 외의 값은 불가
# ba_wrong = bytearray([300, 0.1, "Hello"])


# object()
# 파이썬의 모든 클래스의 기본 클래스로, 새로운 기능 없는 기본 객체를 생성
# isinstance(a,b)는 a가 b라는 클래스의 객체인지 확인하는 것
obj = object()

num_is_obj = isinstance(3.14, object)
str_is_obj = isinstance("안녕", object)


class MyClass:
    pass


cust_class_is_obj = isinstance(MyClass(), object)



# memoryview() , bytearray와 함께 사용 됨
# 바이트 배열 생성 및 크기 조정
data = bytearray(b'hello world!') # (b'문자열') 문자열이 바이트 형식으로 저장됨

# data에 대한 memoryview 생성 memoryview :  data라는 변수의 메모리 주소를 할당
mem_view = memoryview(data)

# memoryview를 사용하여 바이트 배열의 일부를 수정
mem_view[6:12] = b'python'

# 수정된 바이트 배열 출력
print(data.rstrip())

pass