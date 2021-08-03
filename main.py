#함수
#람다
'''
프로그래밍 언어에서는 함수라는 기능을 매개변수로 전달하는 코드를 많이
사용합니다 그리고 이런 코드를 조금 더 효율적으로 작성할 수 있도록 파이썬은
람다(lambda)라는 기능을 제공합니다
'''
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello)


