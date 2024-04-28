# 1. `date`: 연, 월, 일을 다룹니다.
# 2. `time`: 시, 분, 초, 마이크로초를 다룹니다.
# 3. `datetime`: 날짜와 시간을 동시에 다룹니다.
# 4. `timedelta`: 두 날짜나 시간 사이의 기간을 다룹니다.

from datetime import date, time, datetime, timedelta

# 오늘 날짜
today = date.today()    #.today()
t_year, t_monty, t_day = today.year, today.month, today.day     #today.year , today.month , today.day

# weekday 메소드 : 0(월)~6(일) 반환
t_weekday = '월화수목금토일'[today.weekday()]      #[today.weekday()]

# 특정 날짜 생성
some_date = date(2024, 2, 5)
#변수이름.year , 변수이름.month , 변수이름.day 하면 각각의 맞는 숫자들이 나옴
s_year, s_month, s_day = some_date.year, some_date.month, some_date.day



# 현재 시간
now = datetime.now() #년, 월, 일, 시, 분, 초, 마이크로초
n_hr, n_mnt, n_snd, n_msnd = now.hour, now.minute, now.second, now.microsecond
n_yr, n_mth, n_day = now.year, now.month, now.day

# 특정 시간 생성
some_time = time(14, 30)

# 날짜와 시간의 조합 (년,월,일,시,분) 작성하면 설정됨
some_datetime = datetime(2024, 2, 5, 14, 30)



# timedelta를 사용한 연산
ten_days_later = today + timedelta(days=1000) #today는 위에 작성한date.today()
# + timedelta(day=1000)는 1000일 후 날짜를 출력
t_d_l_day = ten_days_later.day
t_d_l_month = ten_days_later.month
t_d_l_year = ten_days_later.year


some_time_later = now + timedelta(minutes=120, seconds=30)
#120분 30초 뒤에 값을 반환 (년,월,일,시,분,초,마이크로초)
s_t_l_hour = some_time_later.hour


# datetime 객체를 문자열로 변환 (포매팅) str , f , time
# 년 : Y , 월 : m , 일 : d , 시 : H , 분 : M , 초 : S
formatted_datetime = now.strftime('%Y - %m - %d %H : %M : %S')

# 문자열로부터 datetime 객체 생성 (파싱) str , p , time  즉 2024-02-05 14:30:00 을 년월일시분초 로 각각 분리한다는 것
parsed_datetime = datetime.strptime('2024-02-05 14:30:00', '%Y-%m-%d %H:%M:%S')
print(parsed_datetime.year)

now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("현재 시각:", formatted_now)

###################예시######################

now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("표준 형식:", formatted_now)

formatted_time = now.strftime("%I:%M:%S %p")
print("12시간 포맷:", formatted_time)

formatted_date = now.strftime("%A, %B %d, %Y")
print("요일, 월, 날짜:", formatted_date)

iso_week_date = now.strftime("%Y-W%W-%w")
print("ISO 주와 연도:", iso_week_date)

log_filename = now.strftime("%Y%m%d_%H%M%S.log")
print("로그 파일명:", log_filename)

just_date = now.strftime("%Y-%m-%d")
just_time = now.strftime("%H:%M:%S")
print("날짜만:", just_date)
print("시간만:", just_time)

formatted_with_tz = now.strftime("%Y-%m-%d %H:%M:%S %Z")
print("시간대 포함:", formatted_with_tz)


pass