# 사용자 지정 예외
# 파이썬에 기본으로 정의되어 있지 않은 예외를 발생시켜야 하는 경우 직접 만들어 사용합니다.

class MonthTypeException(Exception):
    def __init__(self, month): #클래스 생성자 정의
        self.message = f"{month}는 {type(month)}입니다."
        self.code = "123"
        super().__init__("정수를 입력하세요.")
        # 부모클래스(Exception)을 호출하기위해 super()를 사용한 것이고
        #__init__()으로 초기 설정하는데 이때 기본 메세지를 "정수를 입력하세요"라고 예외메세지로 설정한 것
        #만약 def __str__(self)를 사용하지 않는다면 super().__init__으로 설정한 값이 출력됨

#super()는 자식클래스가 부모클래스를 사용할때 사용하는 함수인데
#Exception이라는 파이썬 표준 라이브러리에 내장된 기본 클래스 중 하나라서 (Exception)으로 호출 가능
    def __str__(self): #클래스 반환문 작성
        return f"Error Code {self.code} : {self.message}"
    # 즉 pick_vacation_month(3.14) 로 호출하면 3.14가 int가 아니기때문에
    # MonthTypeException으로 클래스 호출되고 __init__으로 초기 상태 설정
    # 그리고 __str__로 초기 상태 self.code와 self.message를 출력
    # print()함수가 없어도 문자열로 출력 가능 !!!!!


class MonthRangeException(Exception):
    def __init__(self):
        super().__init__("1~12 사이의 숫자를 입력하세요.")



def pick_vacation_month(month):
    try:
        if not isinstance(month, int):
            raise MonthTypeException(month) #raise(예외 발생)시켜 MonthTypeException(month) 클래스 호출 후 리턴받음
        if not 1 <= month <= 12:
            raise MonthRangeException() #raise(예외 발생)시켜 MonthRangeException() 클래스 호출 후 리턴받음

        print(f"{month}월로 휴가 신청 완료되었습니다")

    except MonthTypeException as mte: # 위 MonthTypeException(month) 클래스에서 반환 된것을 가져옴
        mte_str = str(mte)
        print(mte_str) # 🔴

    except MonthRangeException as mre: # 위 MonthRangeException() 클래스에서 반환 된것을 가져옴
        mre_str = str(mre)
        print(mre_str) # 🔴


pick_vacation_month(3)
pick_vacation_month(3.14)
# pick_vacation_month(15)


# # 간단한 Exception 내장 함수 호출 방법
# class MyCustomError(Exception):
#     def __init__(self, message="My custom error occurred"):
#         super().__init__(message)
