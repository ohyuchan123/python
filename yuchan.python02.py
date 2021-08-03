#함수
#재귀 함수로 구현한 피보나치 수열(1)
def fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else :
        return fibonacci(n-1)+fibonacci(n-2)
#함수 호출
print("1! : ",fibonacci(1))
print("2! : ",fibonacci(2))
print("3! : ",fibonacci(3))
print("4! : ",fibonacci(4))
print("5! : ",fibonacci(5))

#재귀 함수로 구현한 피보나치 수열(2)
counter=0
def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter+=1
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#함수를 호출합니다
fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활ㅇㅇ된 덧셈의 횟수는 {}입니다.".format(counter))
