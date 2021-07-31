#반복문
#while 반복문을 for 반복문처럼 사용하기
i=0
while i<10:
    print("{}번째 반복입니다.".format(i))
    i+=1

# while 반복문 : 상태를 기반으로 반복하기
list_test=[1,2,1,2]
value=2

while value in list_test:
    list_test.remove(value)
print(list_test)

#while 반복문 : 시간을 기반으로 반복하기
#5초 동안 반복하기
import time

number=0
target_tick=time.time()+5
while time.time()<target_tick:
    number+=1
print("5초 동안 {}번 반복했습니다.".format(number))
