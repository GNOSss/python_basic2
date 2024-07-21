# 기타 유용한 문법요소
# 아직 다루지 않은, 특히 파이썬의 비교적 최근 버전에 새로 추가된 기능들을 소개합니다.

# 왈러스 연산자 (:=)
# 변수에 값을 할당하면서 이를 즉시 사용하기 위한 연산자입니다.

word = "Hello"
# word = "Hi"

####################################################
letter_count = len(word) # 할당
if letter_count > 3: # 평가
    print(f"통과 (글자 수 {letter_count})")

####################################################
#왈러스 연산자는 약간 다르게 작동함
#우선 len(word) > 3: 이게 맞는지 판별하게되고 , 현재 Hello가 3보다 크니 True를 반환함
#그리고 True를 letter_count에 담다보니 True로 값이 나오게 됨
if letter_count := len(word) > 3: # 💡 할당과 평가가 동시에 이루어짐
    # if 평가할 변수 := 할당할 변수 > 비교연산 :
    print(f"통과 (글자 수 {letter_count})")

#왈러스 연산자를 사용해서 문자열의 길이를 저장하고 싶을때 ()를 통해서
#letter_count 에 len(word)우선적으로 먼저 담고 비교연산 > 3: 을 진행하면 올바른 출력이됨
if (letter_count := len(word)) > 3:

    print(f"통과 (글자 수 {letter_count})")

