#조건문
#불 연산하기 : 논리 연산자
#not : 아니다
#and : 그리고
#or : 또는

#not 연산자
#not 연산자는 단항 연산자로, 참과 거짓을 반대로 바꿀 때 사용합니다
print(not True)
print(not False)

x=10
under_20=x<20
print("under_20",under_20)
print("not under_20",not under_20)

#and 연산자와 or 연산자
#and 연산자는 양쪽 변의 값이 모두 참일 때만 True를 결과로 냅니다
# 반면 or 연산자는 둘 중 하나만 참이어도 True를 결고로 냅니다
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)

