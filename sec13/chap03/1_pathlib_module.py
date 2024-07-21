# pathlib 모듈
# 경로를 객체로 다룸으로써 보다 간결하고 편리하게 파일과 폴더에 관련된 작업을 할 수 있도록 도와줍니다.


from pathlib import Path

# 현재 작업 디렉토리 경로 객체 생성
current_dir = Path('.')         # Path('.') 즉 , 1_pathlib_module.py 현재 경로를 가리킴
                                          # 이후에 Path. 또는 current_dir 를 사용하면 현재 디렉토리 경로를 가리키게 되는 것이다.

# 절대경로(풀 주소) 반환
# absolute()는 현재 경로 기반으로 절대 경로를  반환하고
# resolve()는 심볼릭 링크를 통해 파일 시스템의 실제 경로를 얻음.
# absolute()는 빠르고 간단하지만, 심볼릭 링크의 실제 대상 경로를 제공하지 않음
# resolve()는 정확하고 안전한 경로를 제공하지만 성능 상의 오버헤드가 있을 수 있음
abs_current_dir = current_dir.absolute()
res_current_dir = current_dir.resolve()


# 홈 디렉토리 반환 Path.home()을 사용
home_dir = Path.home()


# 현재 디렉토리 내 항목들
# 현재 작업 디렉토리 경로 객체를 생성한 current_dir 에다가
# .iterdir() 붙여 준다
all_files_curr = [e for e in current_dir.iterdir()]
# all_files_curr = [e for e in current_dir.iterdir()] 의 경우
# current_dir = Path('.') 이 코드의 위치 즉 sec13의 chap03에 위치한 파일과 디렉토리를 for문으로 하나씩 나오게 해줌
print(all_files_curr)
all_files_home = [e for e in home_dir.iterdir()]
# 컴프리헨션을 이용한 for문 사용법이다.



# 특정 파일의 경로 작성 및 존재 여부 확인
tiger = current_dir / "animal" / "Tiger.txt"        #current_dir 을 위에서 작성한 현재 디렉토리 경로를 변수에 담은 것
                                                                       #해당식은 ./animal/Tiger.txt 로 생성해냄
tiger_exists = tiger.exists()       #.exists()는 해당 파일이나 디렉토리 존재 여부를 True/False 로 나타냄



# 파일 삭제 (디버깅이 완료되어야 진행됨)
tiger.unlink(missing_ok=True)  # missing_ok : 없을 시 오류 반환 X


#파일 생성하는 방법
# 1. lion 변수에 경로들 (current_dir / "animal" ) 작성 후 생성할 파일명,형식 ("Lion.txt") 작성
lion = current_dir / "animal" / "Lion.txt"          #주의사항!! lion 변수는 경로를 만드는 것일 뿐 , 파일을 생성하는게 아님
# 2. 파일이 없을 시 생성
# 2-1. 파일을 생성할 경로와 이름이 있는 변수.touch()
lion.touch()
# 만약 lion변수에 있는 파일이 있어도 덮어씌우기로 다시 만들지는 않는다.


# 파일의 텍스트 작성
# 1. 작성할 경로와 이름,형식이 있는 변수.write_text()
# 1-1. (작성할 데이터 입력, 인코딩방식)
lion.write_text(
    "사자는 크고 강력한 고양잇과 동물로, 수컷의 갈기가 특징입니다.",
    "UTF-8"
)



# 부모 폴더 조회
# lion이 가지고 있는 즉, Lion.txt 경로일 것이다. 그리고 그 Lion.txt가 속해있는 폴더를 출력한다.
animal = lion.parent


# 파일 또는 폴더인지 여부
# 동시할당, 튜플 언패킹으로 확인도 가능
lion_is_file, lion_is_dir = lion.is_file(), lion.is_dir()
animal_is_file, animal_is_dir = animal.is_file(), animal.is_dir()


# current_dir 경로에 txt파일을 생성하는 기법
# (경로 / 파일명,형식).touch()
(current_dir / "Hello.txt").touch()
(current_dir / "World.txt").touch()

# 폴더 내 확장자 패턴으로 검색
# 폴더경로.glob("*.확장자") 이렇게 작성하면 확인 가능
# .glob() 는 파일 시스템 내에서 특정 조건에 맞는 파일과 디렉토리 목록을 검색하는데 사용
# list ()형식으로 해야 볼수 있다. 그렇지 않을경우 메모리 주소 값나옴
txts_here = list(current_dir.glob("*.txt"))
pys_here = list(current_dir.glob("*.py"))



# 폴더 내 확장자 패턴으로 재귀적 검색
# rglob() 즉, 특정조건(여기서는 *.txt)으로 current_dir 경로와 하위 경로들을 모두 검색하는데 사용 할 수 있음
txts_rec_here = list(current_dir.rglob("*.txt"))




pass