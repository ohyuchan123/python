#함수
#기본적인 함수의 활용
'''
def 함수(매개변수):
    변수=초깃값
    #여러 가지 처리
    #여러 가지 처리
    #여러 가지 처리
    return 변수
'''
#범위 내부의 정수를 모두 더하는 함수
def sum_all(start,end):
    output=0
    for i in range(start,end+1):
        output+=i
    return output

print("0 to 100 : ",sum_all(0,100))
print("0 to 1000 : ",sum_all(0,1000))
print("50 to 100 : ",sum_all(50,100))
print("500 to 1000 : ",sum_all(500,1000))

#기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수
def sum_all(start=0,end=100,step=1):
    output=0
    for i in range(start,end+1,step):
        output+=i
    return output

print("A.",sum_all(0,100,10))
print("B.",sum_all(end=100))
print("C.",sum_all(end=100,step=2))
