from serialization_class import User
import pickle


# 파일로부터 객체 역직렬화
with open('hong.pickle', 'rb') as file:
    loaded_user_1 = pickle.load(file)

# 역직렬화된 객체의 메소드 호출
greeting = loaded_user_1.greet()

pass

















# 다른 파일에서 클래스,모듈이 담긴걸 꺼낼때는 from 파일명 import 클래스명 을 적어야한다.