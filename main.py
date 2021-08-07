# 모듈
# datetime 모듈
'''
datetime 모듈은 date(날짜),time(시간)과 관련된 모듈로, 날짜 형식을
만들 때 자주 사용되는 코드들로 구성되어 있습니다
'''
import datetime

print("#현재 시각 출력하기")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H.%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, \
                                            now.day,\
                                            now.month, \
                                            now.hour, \
                                            now.minute, \
                                            now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()
