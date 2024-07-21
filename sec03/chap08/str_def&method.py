exp_str = "안녕하세요, Python 클래스입니다. 함께 Python을 배워봐요!"

# 문자열 길이 반환
length = len(exp_str)
len_type = str(type(length))

# 대문자로 변환
upper_case = exp_str.upper()

# 소문자로 변환
lower_case = exp_str.lower()

# 문자열 치환
# 💡 원본을 바꾸지는 않음
replaced_str = exp_str.replace("Python", "파이썬")

# 문자열 분할
split_str = exp_str.split(",")
split_type = str(type(split_str))
aa = split_str[0]

# 문자열 시작 문자열 확인
starts_with = exp_str.startswith("안녕")

# 문자열 종료 문자열 확인
ends_with = exp_str.endswith("니다!")

text_to_search = "Python"
# text_to_search = "Java"

# 문자열 내에 주어신 문자열의 첫 번째 위치 반환
find_result = exp_str.find(text_to_search) #문자열 앞부터 찾음
index_result = exp_str.index(text_to_search)
#찾으려는 문자열이 없을때 find는  -1을 출력 , index 는 오류발생 출력

# 마지막 위치 반환
rfind_result = exp_str.rfind(text_to_search)
#문자열 뒤에서부터 찾음

original_str = "   안녕하세요, 여러분!   "

# 양쪽 공백 제거
stripped_str = original_str.strip()

# 왼쪽 공백 제거
left_stripped_str = original_str.lstrip()

# 오른쪽 공백 제거
right_stripped_str = original_str.rstrip()

# 주어진 문자열을 검사하는 예제 문자열
s = "Hello World 123!"

# isalpha() 메소드는 문자열이 알파벳 문자로만 구성되어 있는지 확인합니다.
is_alpha = s.isalpha()  # 공백과 숫자가 포함되어 있으므로 False를 반환합니다.

# isalnum() 메소드는 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인합니다.
is_alnum = s.isalnum()  # 공백이 포함되어 있으므로 False를 반환합니다.

# islower() 메소드는 문자열의 모든 알파벳 문자가 소문자인지 확인합니다.
is_lower = s.islower()  # 대문자 'H'와 'W'가 포함되어 있으므로 False를 반환합니다.

# isupper() 메소드는 문자열의 모든 알파벳 문자가 대문자인지 확인합니다.
is_upper = s.isupper()  # 소문자와 대문자가 혼합되어 있으므로 False를 반환합니다.

# isspace() 메소드는 문자열이 공백 문자로만 구성되어 있는지 확인합니다.
is_space = s.isspace()  # 알파벳과 숫자가 포함되어 있으므로 False를 반환합니다.

# 결과 출력
print("isalpha: ", is_alpha)
print("isalnum: ", is_alnum)
print("islower: ", is_lower)
print("isupper: ", is_upper)
print("isspace: ", is_space)


pass