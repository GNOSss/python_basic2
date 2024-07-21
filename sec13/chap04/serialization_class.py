import pickle

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"안녕하세요, {self.name}입니다. 나이는 {self.age}살입니다."


user_1 = User("홍길동", 30)
user_2 = User("전우치", 25)


# 객체를 직렬화하여 파일에 저장
with open('hong.pickle', 'wb') as file:
    pickle.dump(user_1, file)



pass