# shutil 실습을 위한 초기화

import os

animal_filename = "Tiger.txt"
animal_description = "호랑이는 크고 강력한 고양잇과 동물로, 아름다운 줄무늬가 특징입니다."

with open(animal_filename, "w", encoding="utf-8") as file:
    file.write(animal_description)

os.makedirs("fruit", exist_ok=True)
os.makedirs("animal", exist_ok=True)

fruits = {
    "Apple.txt": "사과는 달콤하고 아삭아삭한 과일로, 여러 가지 종류가 있습니다.",
    "Banana.txt": "바나나는 영양가가 높고 에너지를 빠르게 제공하는 열대 과일입니다.",
    "Cherry.txt": "체리는 작고 빨간색이며, 달콤하고 약간의 신맛이 나는 과일입니다.",
    "Grape.txt": "포도는 달콤하며 여러 개가 한 송이로 모여 있는 과일입니다.",
    "Orange.txt": "오렌지는 비타민 C가 풍부하고 새콤달콤한 맛이 나는 과일입니다."
}

for filename, description in fruits.items():  # .items()를 사용하여 딕셔너리를 키와 벨류를 분리할 수 있다.
    with open(os.path.join("fruit", filename), "w", encoding="utf-8") as file:
        file.write(description)