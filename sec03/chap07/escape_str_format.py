# print("it's a sunny day")
#
# # 작은따옴표 (Single Quote)
# print('It\'s a sunny day')
#
# # 큰따옴표 (Double Quote)
# print("He said, \"Python is awesome!\"")
#
# # 새 줄 (New Line)
# print("Hello\nWorld")
#
# # 탭 (Tab)
# print("Hello\tWorld")
#
# # 백슬래시 (Backslash)
# print("Backslash: \\") # 💡 백슬래시 하나만 하면 오류
#
# # 백스페이스 (Backspace)
# print("Hello\bWorld")  #'o'가 지워짐
#
# # 캐리지 리턴 (Carriage Return)
# print("Hello\rWorld") # 다시 처음로 돌아감 ('Hello'가 없어짐)

##########문자열 포메팅###########
room_no = 7        # 정수
temp = 21.2     # 실수
label = 'A'       # 문자
owner = 'Alice'   # 문자열

print("방번호 %d, 온도 %f, 라벨 %c, 주인 %s" %(room_no, temp, label, owner))

format_1 = "방번호: %d, 온도: %f°C, 라벨: '%c', 주인: %s." % (room_no, temp, label, owner)

# 소수에 자리수 설정
format_2 = "방번호 %d, 온도: %4.2f°C, 라벨 '%c', 주인: %s." % (room_no, temp, label, owner)

# %s는 다른 자료형도 표시 가능
format_3 = "방번호: %s, 온도: %s°C, 라벨: '%s', 주인: %s." % (room_no, temp, label, owner)

format_4 = "방번호: {}, 온도: {:.2f}°C, 라벨: '{}', 주인: {}.".format(room_no, temp, label, owner)

print("방번호 : {}, 온도 : {:.2f}, 라벨 {}, 주인 : {}.".format(room_no, temp, label, owner))

format_5 = f"방번호: {room_no}, 온도: {temp:.1f}°C, 라벨: '{label}', 주인: {owner}"

print(f"방번호 : {room_no}, 온도 : {temp:.2f}, 라벨: '{label}', 주인 : {owner}")

pass