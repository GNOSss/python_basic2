#특정 조건이 참일 때만 주어진 작업을 수행합니다.
if True:
    print("참입니다.")

if False:
    print("거짓입니다.")



if 3 % 2:
    print("3은 홀수입니다.")
    print("이처럼 들여쓰기로")
    print("여러 줄의 코드를 넣을 수 있습니다.")

if 4 % 2:
    print("4는 홀수입니다.")

if 4 % 2:
    print("4은 홀수입니다.")
else:
    print("4는 짝수입니다.")


letter = "c"
if len(letter) == 1 and ("A" <= letter <= "Z" or "a" <= letter <= "z"):
    print("알파벳 문자입니다.")
else:
    print("알파벳 문자가 아닙니다.")


number = 12
if number < 0:
    print("음수")
elif number == 0:
    print("영")
elif number < 10:
    print("한 자리 숫자")
elif number < 100:
    print("두 자리 숫자")
else:
    print("세 자리 이상 숫자")

age = 21
is_student = False
if age >= 20:
    if is_student:
        print("할인가")
    else:
        print("정가")
else:
    print("판매제한")