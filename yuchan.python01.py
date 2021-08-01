#함수
#함수의 기본
'''
def 함수 이름():
    문장
'''
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
print_3_times()

print()
#매개변수의 기본
def print_n_times(value,n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요",5)
