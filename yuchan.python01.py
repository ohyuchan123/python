#함수
#재귀 함수
'''
팩토리얼(factorial)
n!=n*(n-1)*(n-2)*...*1
'''
#반복문으로 팩토리얼 구하기
def factorial(n):
    output=1
    for i in range(1,n+1):
        output*=i
    return output

#함수 호출
print("1! : ",factorial(1))
print("2! : ",factorial(2))
print("3! : ",factorial(3))
print("4! : ",factorial(4))
print("5! : ",factorial(5))



