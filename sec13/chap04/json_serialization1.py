import json

# 복잡한 데이터 구조를 가진 딕셔너리
data = {
    "name": "홍길동",          #문자
    "age": 30,          #정수
    "is_employee": True,        #불리언
    "education": [          #딕셔너리
        {"school": "낙성대", "degree": "bachelor"},
        {"school": "태종대", "degree": "master"}
    ],
    "skills": ["Python", "Machine Learning", "Web Development"]     #리스트
}

# 딕셔너리를 JSON으로 변환하고 파일로 저장
with open('data.json', 'w', encoding="UTF-8") as f:
    #저장할 경로 및 이름 , 모드 , 인코딩방식(한글) as f <<참조 변수
    json.dump(data, f, indent=4)
    #json형식으로 dump(저장기능)
    #indent = 4는 json 매개변수 각 라인을 새로 들여쓰기할 공백의 수를 정의함.
    #즉 indent = 4 의 4는 4개의 공백을 추가하여 들여쓰기 한다는 의미

    # json.dump(data, f, ensure_ascii=False, indent=4)
    # 이렇게 저장하면 json파일에 한글도 저장가능함.

