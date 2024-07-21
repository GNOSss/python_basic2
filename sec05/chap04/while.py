#주어진 조건을 충족시키는 동안 작업을 반복합니다.

# i = 0
#
# while i < 5:
#     print(i)
#     i += 1


# my_list = ["사과", "바나나", "체리"]
# i = 0
#
# while i < len(my_list):
#     print(my_list[i])
#     i += 1


# 역시 break와 continue 사용 가능
# i = 0
#
# while i < 20:
#     i += 1
#     if i % 2 == 0:
#         continue
#     if i > 10:
#         break
#     print(i)


# x = 0
#
# while True:
#     print(x)
#     x += 1


# print("끝말잇기 게임을 시작합니다. '종료'를 입력하면 게임이 끝납니다.")
#
# last_word = input("첫 단어를 입력하세요: ").strip()
#
# while True:
#                                     #{last_word[-1]은 문자열의 마지막 단어를 표시함
#     next_word = input(f"{last_word[-1]}로 시작하는 단어를 입력하세요: ").strip()
#
#     if next_word == "종료":
#         print("게임을 종료합니다.")
#         break
#     #last_word[-1] 이전 단어의 마지막열과 next_word[0] 현재 단어 첫글자랑 다르다면 !이라는 뜻
#     if last_word[-1] != next_word[0]:
#         print(f"잘못된 단어입니다. '{last_word[-1]}'(으)로 시작해야 합니다.")
#         continue # 아래의 코드가 실행되지 않고 다음 턴으로
#     # 위의 if문 2개 모두 해당되지 않으면 next_word를 last_word로 담는다.
#     last_word = next_word