### `try ... except ... else ... finally`

# - `try` : 예외가 발생할 수 있는 구문
# - `except` : 예외가 발생했을 시 실행
# - `else` : 예외가 발생하지 않았을 시 실행
# - `finally` : 예외가 발생하든 않든 실행


# nums = [1, 2, 3, 4, 5]
# my_input = input("10을 나눌 숫자를 입력하세요 : ")
#
# try: #예외가 발생할 수 있는 코드를 작성해본다
#     my_input_int = int(my_input)
#     to_add = nums[my_input_int]
#     print(10 / my_input_int + to_add, end=" ")
#
# except: # 모든 종류의 오류를 다 처리 # try 구문에 오류발생시 except 실행
#     print("⚠️ 오류 발생")
# else: # 오류가 발생하지 않으면 else 구문 실행 # else문은 필수가 아님
#     print("✅")
# # try 구문을 끝까지 실행했으니 print("무사히 실행") 도 진행
# print("무사히 실행!")




# nums = [1, 2, 3, 4, 5]
# my_input = input("10을 나눌 숫자를 입력하세요 : ")
#
# try:
#     my_input_int = int(my_input)
#     to_add = nums[my_input_int]
#     print(10 / my_input_int + to_add, end=" ")
#
# except Exception as e: # as e를 붙혀줌으로써 예외에 대한 원인을 출력으로 알려줄 수 있음
                                    # 중요한건 except 다음으로 Exception 을 사용해서 원인을 알 수 있음
#     print(f"⚠️ 오류 발생 {e}")
# else:
#     print("✅")
#
# print("무사히 실행!")
# # as e  는 꼭 붙여야 하는 것은 아님 (e 를 아래에 사용할 것이 아니라면)




# 오류의 종류별로 예외문 작성
# nums = [1, 2, 3, 4, 5]
# my_input = input("10을 나눌 숫자를 입력하세요 : ")
#
# try:
#     my_input_int = int(my_input)
#     to_add = nums[my_input_int]
#     print(10 / my_input_int + to_add, end=" ")
#
# except ValueError as e:
#     print(f"⚠️ 숫자가 아님 {e}")
# except IndexError as e:
#     print(f"⚠️ 범위가 틀렸음 {e}")
# except Exception as e:
#     # ValueError(숫자) IndexError(범위)도 아닌 오류(Exception)은 나중에 넣을 것
#     print(f"⚠️ 오류 발생 {e}")
#
# print("무사히 실행!")





nums = [1, 2, 3, 4, 5]
my_input = input("10을 나눌 숫자를 입력하세요 : ")

try:
    my_input_int = int(my_input)
    to_add = nums[my_input_int]
    print(10 / my_input_int + to_add, end=" ")

except (ValueError, IndexError) as e:
    #except(@, @, @) as @: 이런식으로 여러 예외코드를 작성해서 사용 가능
    print(f"⚠️ 숫자가 아니거나 범위를 벗어남 {e}")
except Exception as e:
    print(f"⚠️ 오류 발생 {e}")

print("무사히 실행!")




# finally 사용
# 예외 발생 여부와 무관하게 사용
# 함수의 return과 무관하게 실행

def my_calculation(num):
    nums = [1, 2, 3, 4, 5]

    try:
        my_input_int = int(num)
        to_add = nums[my_input_int]
        result = 10 / my_input_int + to_add
        print("✅ 정상 작동")
        return result # 함수를 종료

    except: # 모든 종류의 오류를 다 처리
        print("⚠️ 오류 발생!")
        return float('nan') # 함수를 종료

    finally: # 💡 try 또는 except에서 return을 해도 실행
        print("🙆 함수 실행 종료\n- - - - -\n")

    # finally 대신 아래를 활성화 해 볼 것
    print("🙆 함수 실행 종료\n- - - - -\n")

# filnally 사용 없이 def my_calculation 함수에 print("🙆 함수 실행 종료\n- - - - -\n") 이걸 사용할 수 없음
# 왜냐하면 try 와 except 에 return이 존재하면 return은 그 값을 반환하고 def 함수를 종료하는 것이기 때문이다.


print(my_calculation(1))
print(my_calculation(0))
print(my_calculation('a'))

# GPT4 _ finally 필요성
# finally의 필요성
# 리소스 해제 보장: 프로그램에서 파일, 데이터베이스 연결, 네트워크 세션과 같은 리소스를 사용할 때,
# 이를 적절히 해제해주지 않으면 리소스 누수가 발생할 수 있습니다.
# finally 블록은 예외 발생 여부와 관계없이 이러한 리소스를 반드시 해제할 수 있도록 해 줍니다.
# 정리 작업 수행: 프로그램에서 임시 파일 생성, 로그 기록 등 일시적인 작업을 수행하는 경우,
# 이러한 작업들을 정리하는 코드를 finally에 배치하여 항상 실행되도록 할 수 있습니다.
# 프로그램의 흐름 명확화: 예외가 발생했을 때 어떤 코드는 실행되고 어떤 코드는 실행되지 않는 상황을 피하고
# 프로그램의 종료 단계에서 반드시 실행해야 하는 로직을 finally에 배치함으로써 프로그램의 흐름을 명확하게 할 수 있습니다.