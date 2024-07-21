# 폴더 다루기

import os
import time


# 폴더 이름 정의
folder_name = 'fruits'

# 폴더 생성
if not os.path.exists(folder_name):
    os.makedirs(folder_name)  #os.makedirs() 디렉토리를 생성하는 명령어

# 또는 아래와 같이 작성
# exist_ok = True 는 이미 같은 디렉토리가 있어도 생성하겠다 또는 에러를 발생하지 않겠다는 명령어
os.makedirs(folder_name, exist_ok=True)

# 파일 생성 및 내용 쓰기
fruits = ['apple', 'orange', 'mango']
for fruit in fruits:  # fruits 리스트의 요소를 1개씩 순회시킴
    file_path = os.path.join(folder_name, f'{fruit}.txt') # os.path.join으로 파일 경로 생성함 , 첫 순회의 경우 file_path : 'fruits/apple.txt'가 되겠음
    with open(file_path, 'w') as file: #file_path 경로에 파일을 쓰기 모드로 열고 file 변수로 참조한다.
        file.write(fruit) # file변수에 존재하는 경로의 파일을 찾아 fruit 변수에 있는 내용을 작성



# 폴더 내 모든 파일명 출력
# os.listdir() 함수는 folder_name 내의 모든 파일 및 디렉토리 이름을 나열하고 출력하는 기능을 수행
file_names = os.listdir(folder_name)
print(f"'{folder_name}' 폴더 내 파일 목록:", file_names)
# print()문에서 ( , file_names) 을 해야지 출력됨


# 모든 파일의 내용 출력
for file_name in file_names: #file_names 는 apple.txt , mango.txt , orange.txt 로 구성됨
    file_path = os.path.join(folder_name, file_name)
    # os.path.join() 사용할때 논리적인 순서에 따라야함 (디렉토리에서 하위 디렉토리 또는 파일)
    # 가능한 파일명보다는 경로를 작어주는게 좋음(?)
    with open(file_path, 'r') as file:
        print(f"'{file_name}'의 내용:", file.read())
# print()문에서 ( , file.read) 을 해야지 출력됨




# 여러가지 os.path 툴 (디버깅 해볼 것)
apple_joined = os.path.join(folder_name, "apple.txt") #현재 2_basic_use_folder.py의 상대적 경로

apple_abs = os.path.abspath(apple_joined) # 절대 경로를 표시

apple_dir = os.path.dirname(apple_joined) #디렉토리 이름 반환
apple_base = os.path.basename(apple_joined) #파일 이름 반환

apple_is_file = os.path.isfile(apple_joined) #파일이 맞는지 여부 확인
apple_is_dir = os.path.isdir(apple_joined) #디렉토리가 맞는지 여부 확인

apple_size = os.path.getsize(apple_joined) # 사이즈 확인 (byte)

pass



# 폴더 안의 모든 파일 삭제 및 폴더 삭제
for file_name in file_names:    # 리스트 형식의 file_names: 를 file_name으로 순회하고
    # file_name에 있는 것들을 (디렉토리 경로 = folder_name , 파일 명 = file_name) 으로 삭제(os.remove)
    os.remove(os.path.join(folder_name, file_name))
# os.rmdir() folder_name 삭제
os.rmdir(folder_name)