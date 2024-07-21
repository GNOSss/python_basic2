#“값이 없음”을 나타내기 위한 자료형입니다.
#타 언어들의 null, nil과 유사합니다.
#값이 들어오는/나올 수 있는 곳에서 값이 없을 때 들어오는/나오는 값

non = None
non_type = str(type(non))

non_1 = None
non_1_id = id(non_1)

non_2 = None
non_2_id = id(non_2)

non_3 = None
non_3_id = id(non_3)

# 때문에 값이 None인 것들끼리는 is()가 True 반환
all_same = non_1 is non_2 is non_3

var_1 = None
var_2 = 1

# == 대신 is 함수 권장
# 싱글턴 객체 'None'은 여러 메서드를 사용하여 비교함, 가독성 문제도 있음
# GPT에 물어보셈
is_none_1 = var_1 is None
is_none_2 = var_2 is None

pass