import threading
import time

# 쓰레드에서 실행할 함수 정의
def print_numbers():
    for i in range(1, 6):
        time.sleep(1)
        print(f"Number: {i}")

def print_letters():
    for letter in 'abcde':
        time.sleep(1.5)
        print(f"Letter: {letter}")

# 쓰레드 객체 생성
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# 쓰레드 시작
thread1.start()
thread2.start()

# 모든 쓰레드가 종료될 때까지 기다림
thread1.join()
thread2.join()

print("All threads have finished.")
