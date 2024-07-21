import threading
import time

# 쓰레드에서 실행할 함수들
def print_numbers():
    # 1부터 5까지 숫자를 출력
    for i in range(1, 6):
        time.sleep(1)
        print(f"Number {i}")

def print_letters():
    # A부터 E까지 문자를 출력
    for letter in "ABCDE":
        time.sleep(1)
        print(f"Letter {letter}")


thread_1 = threading.Thread(target=print_numbers)
thread_2 = threading.Thread(target=print_letters)

thread_1.start()
thread_2.start()
print("쓰레드 시작 직후")

thread_1.join()
thread_2.join()
print("쓰레드 종료")