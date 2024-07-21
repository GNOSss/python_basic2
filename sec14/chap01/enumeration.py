# 열거형 (enumeration)
# 특정 종류의 데이터에 정해진 값들 중 하나만 들어갈 수 있도록 하는 것을 말함
# 파이썬의 열거형은 enum 패키지를 통해 제공됩니다.

from enum import Enum, unique, auto


# unique 데코레이터 : 겹치는 값이 없는지 확인
# ⚠️ 겹치게 하고 실행해 볼 것
@unique
class Weekday(Enum):        #Weekday클래스가 Enum이라는 패키지 안에 클래스들을 상속받을 수 있게 설정
    # import unique 는 각 변수에 할당되는 값들이 중복이 안되게끔 설정하는 기능 (만약 값 1이 2번 나타나면 오류발생)
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# auto : 자동으로 값 할당
class Hand(Enum):       #Hand클래스가 Enum이라는 패키지 안에 클래스들을 상속받을 수 있게 설정
    # import auto 는 따로 값을 정하지 않았을때 설정한다.
    # 즉  ROCK, PAPER,SCISSORS 같은 변수가 중요할때 사용하면 됨
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


for day in Weekday:
    print(day.name, day.value)
# 열거형 Enum을 사용할때 .name을 사용하면 변수명 호출되고
# .value를 사용하면 값(상수형)이 호출된다.

for hand in Hand:
    print(hand.name, hand.value)


# 열거형 Enum의 Weekday클래스에 속한 변수명이자 .name인 MONDAY를 today에 담는다.
# 즉 value = 1  을 갖고있는 것
today = Weekday.MONDAY
# today = Weekday.SUNDAY

tomorrow = Weekday((today.value + 1) % 7) # 값으로 열거형 객체 생성


def determine_winner(player_one, player_two):
    win_map = {
        Hand.ROCK: Hand.SCISSORS,  # 바위는 가위를 이김
        Hand.PAPER: Hand.ROCK,  # 보는 바위를 이김
        Hand.SCISSORS: Hand.PAPER  # 가위는 보를 이김
    }

    if player_one == player_two:
        return "Draw"
    # win_map 딕셔너리에 player_one 의 값을 Key 전달해 그에 맞는 Value 값과 player_two 값이 일치하는 보는 것
    elif win_map[player_one] == player_two:
        return "Player One Wins"
    else:
        return "Player Two Wins"


player_one_hand = Hand.ROCK
player_two_hand = Hand.SCISSORS
#determine_winner 함수에 (player_one_hand, player_two_hand) 값을 인자로 넣어고 호출
game_result = determine_winner(player_one_hand, player_two_hand)
