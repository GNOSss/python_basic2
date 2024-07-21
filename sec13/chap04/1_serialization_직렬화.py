# 직렬화(serialization)란 각종 형태의 데이터를 전송 가능한 형태로 변환하는 과정을 말합니다.
# 이를 다시 데이터로 변환하는 과정은 역직렬화(deserialization)라고 합니다
# 파이썬의 직렬화 : pickle 모듈 사용

import pickle

my_list = ['apple', 'banana', 'cherry']
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# 데이터를 pickle 파일로 저장
# 'wb'는 write binary 모드 (쓰기 + 이진법)
# pickle.dump(입력할 변수, with open 정보의 변수 <<여기서는 f )
with open('my_data.pickle', 'wb') as f:
    pickle.dump(my_list, f)
    pickle.dump(my_dict, f)







pass