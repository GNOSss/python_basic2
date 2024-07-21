import json

# class의 def area,perimeter 같은 메소드는 Json 형식으로 저장할 수 없다
# __init__ 속성만 json 형식으로 저장할 수 있어서 하단에 응용하는 방법을 참고

class Rectangle:
    border_color = "black"

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# 클래스안에 하단의 함수 같은 걸 생성해서 위의 def area, perimeter 함수의 값을 도출해서 json으로 저장할 수 있음
# def to_dict 가 rect.__dict__ 가 할 수 없는 def area,perimeter 까지 다 처리할 수 있음
    def to_dict(self):
        return {
            "border_color": Rectangle.border_color,
            "width": self.width,
            "height": self.height,
            "area": self.area(),
            "perimeter": self.perimeter()
        }




#클래스 호출과 인스턴스 생성
rect = Rectangle(3, 4)



# 💡 객체의 속성들을 딕셔너리로
# 클래스 변수, 메소드 등은 포함하지 않음
# __dict__ 는 rect 변수가 갖고있는 Rectangle 클래스에 (3,4) 인스턴스를 불러서 속성(self.width,height)를 생성함
rect_dict = rect.__dict__       #즉 rect_dict = {'height':4 , 'width':3}의 형태가 됨



# with open('rect.json', 'w', encoding="UTF-8") as f:
#     json.dump(rect_dict, f, indent=4)

    # ⚠️ 커스텀 객체는 기본적으로 JSON으로 직렬화되지 않음
    # json.dump(rect, f, indent=4)

# 응용한 def to_dict(self): 로 새로운 json 파일을 만들어 냄
with open('rect_obj.json', 'w', encoding="UTF-8") as f:
    json.dump(rect.to_dict(), f, indent=4)
                # rect 변수로 Rectangle 클래스 호출 그리고 to_dict 함수 호출
pass