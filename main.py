#반복문
#리스트 연산자 : 연결(+),반복(*),len()

#리스트를 선언합니다
list_a=[1,2,3]
list_b=[4,5,6]
#출력합니다
print("#리스트")
print("list_a=",list_a)
print("list_b=",list_b)
print()
#기본 연산자
print("#리스트 기본 연산자")
print("list_a+list_b=",list_a+list_b)
print("list_a*3=",list_a*3)
print()
#함수
'''
len() 함수는 괄호 내부에 문자열을 넣으면 문자열의 글자 수(=길이)를 세어 주지만, 리스트 
변수를 넣으면 요소의 개수를 세어 줍니다. 19행은  list_a에 들어있는 요소의 개수를 구합니다
'''
print("#길이 구하기")
print("len(list_a)=",len(list_a))
