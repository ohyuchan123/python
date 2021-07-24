#조건문
#날짜/시간 활용하기
#날짜/시간
import datetime

#현재 날짜/시간을 구합니다.
now=datetime.datetime.now()

#출력합니다.
print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")

#datetime.datetime.now()라는 함수로 현재의 시간을 구해 now라는 변수에 대입합니다

#출력합니다[방법 2]
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))