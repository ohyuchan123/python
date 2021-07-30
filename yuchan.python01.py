#반복문
#범위
a=range(5)
print(a)
print(list(range(10)))
print(list(range(0,5))) #0부터 (5-1)까지의 정수로 범위를 만듭니다
print(list(range(0,10,2))) #0부터 2씩 증가하면서 (10-1_까지의 정수로 범위를 만듭니다

a=range(10+1)
print(list(a))

n=10
a=range(0,int(n/2))#->실수를 정수로 바꾸는 방법보다
print(list(a))
a=range(0,n//2)#->정수 나누기 연산자를 많이 사용합니다
print(list(a))