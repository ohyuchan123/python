#모듈
#시간 처리하기
import datetime
now=datetime.datetime.now()

print("# datetime.timedelta로 시간 더하기")
after=now+datetime.timedelta(
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1,
)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

print("# now.replace()로 1년 더하기")
output=now.replace(year=(now.year+1))
print(output.strftime(("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")))