# 가상환경
# 파이썬의 가상환경은 프로젝트마다 사용되는 라이브러리들과 그 버전들,
# 파이썬 인터프리터 등을 구분하기 위해 사용됩니다.


# "env1"이라는 이름의 가상환경 생성
# python3 -m venv env1
# 여기서 env1 말고 사용자가 임의대로 이름 작성가능


# 가상환경 활성화
# 윈도우 : env1\Scripts\activate
# 맥,리눅스 : source env1/bin/activate
# 해당 명령어를 터미널에서 활성화하면
# 사용자가 작성한 가상환경(여기선 env1)을 위한 터미널이 활성화됨

# 가상환경 비활성화
# deactivate
# 패키지 다시 확인할 것 (pip list)


# 패키지 정보 확인
# pip show @@@ << numpy , pandas 등등