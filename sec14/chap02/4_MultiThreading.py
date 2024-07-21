import threading
import random
import time


def print_data(thread_name, data):
    for item in data:
        time.sleep(
            # 💡 1 ~ 1.5 사이의 무작위 수 생성
            random.uniform(1, 1.5)
        )
        print(f"{thread_name} : {item}")


threads = []

for i in range(10):
    thr = threading.Thread(
        target=print_data,
        args=(f"Thread No.{i + 1}", range(10))
    )
    threads.append(thr)

for thr in threads:
    thr.start()
    # thr.join() # ⚠️ 활성화시켜 볼 것

#thr.start()가 다 끝날때까지 기다림
for thr in threads:
    thr.join()

print("- - - - -\n쓰레드 작업 종료")