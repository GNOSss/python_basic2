# 파일과 폴더 다루기
# 파일과 폴더를 생성/수정/삭제하는 기본적인 방식입니다.

# 파일과 디렉터리(폴더) 관리할때 os 모듈이 필요함
# 물론 os 모듈로  환경 변수 접근, 경로 관리, 프로세스 관리, 시스템 정보 접근 등을 할 수 있다.
import os

# 변수명 상관없이 "first_file.txt" 쓰는데 경로가 없으면 현재 작성중인 파이썬 파일 경로로 주소가 찍힘
file_path = "first_file.txt"

# 파일 존재 여부 확인
# os.path.exists(파일경로가 담긴 변수명)
file_exists = os.path.exists(file_path)


# os 모듈로 현재 작업중인 파일 경로 출력
print(f"내가 작업중인 위치는 {os.getcwd()} 이다")



# 파일 열기
# with : 파일을 열 때 사용하며 사용 후 파일을 자동으로 닫아줌
# open : 파일을 여는데 사용되는 함수
# - 두 번째 인자 : 모드
#     - `r` (기본) : 읽기
#     - `w` : 쓰기 (있던 파일을 열어서 'w'하면 기존 것들 없어짐)
#     - `a` : 추가
#     - `+` : 읽기&쓰기

# as file: 은 with 블록 안에서만 사용 가능하며 as file의 file이 file_path를 가르키는 것이다.
# 즉 as file 의 file -> file_path -> first_file.txt 를 가르킴

# with open(file_path, 'r') as file:
#     file_content = file.read()
# print(f"파일 내용:\n{file_content}")

# 보다 안전한 코드 (위에 코드는 기본적인 파일을 여는 코드인데 간혹 없는 파일이라면 아래처럼 예외문을 넣어줌)
# try:
#     with open(file_path, 'r', encoding="UTF-8") as file:   #한글이 포함된 텍스트라면 encoding = "UTF-8"을 입력
#         file_content = file.read()
#     print(f"파일 내용:\n{file_content}")
# except Exception as e:
#     print(f"⚠️ 파일 읽기 중 오류 발생: {e}")


# 파일 쓰기 (file_path 경로는 상단에 file_path = "first_file.txt" 라고 적어둠
try:
    with open(file_path, 'w') as file:
        file.write('Hello, world!')
except Exception as e:
    print(f"⚠️ 파일 쓰기 중 오류 발생: {e}")

# 내용 추가하기
try:
    with open(file_path, 'a', encoding="UTF-8") as file:  #한글이 포함된 텍스트라면 encoding = "UTF-8"을 입력
        for fruit in ["사과", "배", "귤"]:
            file.write(f"\n{fruit} 사세요.")
except Exception as e:
    print(f"⚠️ 파일 내용 추가 중 오류 발생: {e}")



# 파일 삭제
if os.path.exists(file_path): # 파일 존재 여부 확인
    os.remove(file_path) # 💡 존재하지 않는데 실행되면 에러  / os.remove()는 파일 삭제 명령어
    print(f"{file_path} 파일이 삭제되었습니다.")
else:
    print(f"{file_path} 파일이 존재하지 않습니다.")