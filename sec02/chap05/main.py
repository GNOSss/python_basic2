# 각종 값을 저장하는 변수들

last_name = "홍"
first_name = "길동"

age = 22

married = False

print(last_name, first_name, age, married)


# 변수사용예제 - 지금은 이해할 필요 없음

print(f"저는 {age}살입니다.")
print(f"만으로는 {age - 1}살이죠.")
print("자격 : " + ("있음" if age > 20 else "없음"))
for candle in range(age):
    print("🕯️", end="")

x, y, z = True, 2, "삼"
pass