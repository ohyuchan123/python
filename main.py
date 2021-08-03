#함수
#재귀 함수를 사용해 팩토리얼 구하기
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

#함수 호출
print("1! : ",factorial(1))
print("2! : ",factorial(2))
print("3! : ",factorial(3))
print("4! : ",factorial(4))
print("5! : ",factorial(5))