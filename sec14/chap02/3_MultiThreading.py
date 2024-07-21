import threading
import time


def print_data(data):
    for item in data:
        time.sleep(1)
        print(item)


# 💡 인자와 함께 쓰레드 생성
# ⚠️ 인자는 컬렉션 형태로 넣어야 함
                                                            #range(5),) 이것은 값 하나만 포함하는 튜플이라는 뜻
                                                            #args 매개변수는 튜플형식으로 인자들을 전달받지 못함
                                                            #튜플을 정의할때 (5) 이렇게 하나만 있는 경우 (,)로 붙여야된다고함
                                                            #(range(5),)는 요소가 하나인 튜플입니다.
                                                            #(range(5))는 range(5)라는 표현식입니다.
t1 = threading.Thread(target=print_data, args=(range(5),))
t2 = threading.Thread(target=print_data, args=["ABCDE"])

t1.start()
t2.start()
# time.sleep()함수가 없었으면 간단한 식에서는 먼저 시작해서 끝나고 다음께 시작하고 끝나지만
# time.sleep()을 같이 실행하면 거의 동시 실행하면서 출력값이 규칙적으로 출력되지 않음
