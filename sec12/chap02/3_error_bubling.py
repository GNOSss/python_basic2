class MySyntaxError(Exception):
    pass


class MyTypeError(Exception):
    pass


class MyReferenceError(Exception):
    pass

def func1(e):  # 사원
    try:
        if e: raise e   # if e: 가 True일 경우 raise e 를 실행한다. False일 경우 하단 print()함수 실행
        print('저 가 봐도 되죠?')
        print('- - - - - - - - - -')

    except MySyntaxError as e:
        print('저 이건 알아요!', e)
        print('- - - - - - - - - -')
        return
    except Exception as e:  # 파이썬에서는 모든 예외의 기본 클래스는 Exception입니다.
        print('대리님, 이거 뭐에요?')
        raise e  # 처리하지 못하는 에러는 (func2)로 던짐


def func2(e):  # 대리
    try:
        func1(e)
    except MyTypeError as e:
        print('내가 할 테니 가봐요.', e)
        print('- - - - - - - - - -')
        return
    except Exception as e:
        print('부장님, 이건 제 선에서 안 되겠습니다.')
        raise e # 처리하지 못하는 에러는 (func3)로 던짐


def func3(e):  # 부장
    try:
        func2(e)
    except MyReferenceError as e:
        print('잘 하자, 응?', e)
        print('- - - - - - - - - -')
        return
    except Exception as e:
        print('사장님, 이것 좀 보셔야겠습니다.')
        raise e # 처리하지 못하는 에러는 (func4)로 던짐


def func4(e):  # 사장
    try:
        func3(e)
    except Exception as e:
        print('전원 집합.', e)



func4(None)
func4(MySyntaxError)
func4(MyTypeError)
func4(MyReferenceError)
func4(Exception)