#함수
#키워드 매개 변수
'''
print(value,...,sep=' ',end='\n',file=sys.stdout,flush=False)
이름을 지정해서 입력하는 매개변수를 키워드 매개변수라고 부릅니다
'''
def print_n_times(*values,n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

#함수 호출
print_n_times("안녕하세요","즐거운","파이썬 프로그래밍",n=3)

#열 함수 호출 형태
def test(a,b=10,c=100):
    print(a+b+c)
#1)기본 형태
test(10,20,30)
#2)키워드 매개변수로 모든 매개변수를 지정한 형태
test(a=10,b=100,c=200)
#3)키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c=10,a=100,b=200)
#4)키워드 매개변수로 일부 매개변수만 지정한 형태
test(10,c=200)
