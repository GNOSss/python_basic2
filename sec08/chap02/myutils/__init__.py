#  `__init__.py` : 패키지를 `import` 할 때 필요
#  3.3 버전 이후부터는 없어도 기본적으로 동작
#  패키지 초기화 구조를 정의하기 위해 여전히 사용됨

print("myutils가 임포트되었습니다.")

# from . import subutils
# 위를 활성화하고 다시 실행해볼 것
#  __init__.py에서는 상대경로 사용 ( . )


from .arithmetics import add
# from 현재경로(.)파일명 import 메소드명


from .subutils import all_arith_print as arith_example
# subutils 폴더의 init 파일안에 있는 함수 all_arith_print 를 Import함
# 대신 현재 파일에서는 arith_example 이라는 호출명으로 사용

print("사용할 수 있는 산술연산 예시:")
arith_example(3, 4)