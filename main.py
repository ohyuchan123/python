#함수
#가변 매개변수
'''
def 함수이름(매개변수,매개변수,...,*가변 매개변수):
    문장
'''

#가변 매개변수 함수
def print_n_times(n,*values):
    for i in range(n):
        for value in values:
            print(value)
        print()

#함수 호출
print_n_times(3,"안녕하세요","즐거운","파이썬 프로그래밍")

#기본 매개변수
'''
print(value,...,sep=' ',end='\n',file=sys.stdout,flush=False)
'''
#기본 매개변수
def print_n_times(value,n=2):
    for i in range(n):
        print(value)

#함수 호출
print_n_times("안녕하세요")