# 에러 버블링
# 함수가 다른 함수를 호출할 경우, 하위 함수에서 발생한 에러가 상위 함수로 전달되는 것을 말합니다.

#### 아래 식 설명문 ####
# 총 func1,2,3,4가 있음
# func4가 func3을 ,  func3이 func2를 , func2가 func1를 가르키고 있음
# 그리고 func1(마지막 내장함수)가 raise Exception (예외) 를 발생했는데
# 예외처리는 func4가 처리해야됨
# 그리하여 func1,2,3의 print("func 완료")가 처리되지 못함
# 왜 ? func1,2,3,4의 print("func 실행") 문 밑에 모두 다른 함수들을 호출하는데
# 예외발생 후 처리가 되지 않아서 print("func 완료")가 출력되지 않고
# func4에서 try ... except ... 로 처리하고 func4에서 print("func4 완료")라고 출력됨

# 25번째 줄을 없애고 26~29번째 줄을 활성화하면 func2가 func1에서 발생시키 예외처리를 바로잡고 나머지 print("func2,3,4 완료") 작업을 하게됨

def func1():
    print("func1 실행")
    raise Exception('에러 발생')
    print("func1 완료")


def func2():
    print("func2 실행")

    func1() # 아래로 대체해 볼 것
    # try:
    #     func1()
    # except Exception as e:
    #     print(f"{e} 처리")

    print("func2 완료")


def func3():
    print("func3 실행")
    func2()
    print("func3 완료")


def func4():
    print("func4 실행")

    try:
        func3()
    except Exception as e:
        print(f"{e} 처리")

    print("func4 완료")


func4()