### 프로세스와 쓰레드

# - 프로세스 *process*
#     - 각 프로그램마다 진행
#     - 각각 메모리 공간을 할당받음
#         - 코드, 데이터, 기타 시스템 자원
#         - 기본적으로는 프로세스간 공유되지 않음
#     - 생성시 비교적 많은 시간과 메모리 소모
#     - 종료시 프로그램 종료
# - 쓰레드 *thread*
#     - 한 프로세스 안에 여럿 생성되어 진행될 수 있음
#         - 업데이트를 받으면서 코딩을 계속할 수 있는 이유
#     - 프로세스 내의 자원을 여러 쓰레드가 공유
#         - ⚠️잘못 다루면 위험
#     - 프로세스보다 생성 부담이 적음


import threading
import time


# 쓰레드에서 실행할 작업
def print_numbers():

    for i in range(1, 6):
        time.sleep(1) # 💡 1초 대기
        print(f"Number {i}")


# 쓰레드 객체 생성 / 변수 = threading(모듈).Thread(클래스)(target=함수명)
thread_1 = threading.Thread(target=print_numbers)


# 쓰레드 시작 / 쓰레드변수.start()
thread_1.start()
print("쓰레드 시작 직후")
### code run 해보면 알겠지만
### threading.Thread를 사용했다는건 Main Thread가 아닌 다른 Thread를 생성해 작업하는 것이기에
### print("쓰레드 시작 직후") 구문이 thread_1.start()보다 밑에 있지만
### 먼저 출력되는 걸 알 수 있다.
### 물론 time.sleep(1)이 있어서 늦게 시작하는 것임
### time.sleep(1) 없었으면 thread_1.start()가 더 빠르게 나옴 , 또 대용량이면 결과물 달라 질 것


# 메인 쓰레드에서 해당 쓰레드 종료를 기다림
# thread_1.join() 이 없었으면 thread_1.start()가 다 끝나기도 전에 print("쓰레드 종료")가 출력 되었을 것이다.
thread_1.join()
print("쓰레드 종료")


