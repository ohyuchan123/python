#조건문
#if 조건문
#if 조건문은 조건에 따라 코드를 실행하거나, 실행하지 않게 만들고 싶을 때 사용
#하는 구문입니다

if True:
    print('True입니다..!')
    print('정말 True입니다..!')

if False:
    print('False 입니다...!')

#조건문 기본 사용
number=input("정수 입력>")
number=int(number)

#양수 조건
if number>0:
    print("양수 입니다")
#음수 조건
if number<0:
    print("음수 입니다")
#0 조건
if number==0:
    print("0입니다")
