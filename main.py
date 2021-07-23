#자료형
#대소문자 바꾸기 : upper()와lower()
#upper() 함수는 문자열의알파벳을 대문자로,lower() 함수는 문자열의 알파벳을 소문자로 만듭니다
a="HEllo Python Programmin...!"
print(a.upper())
print(a.lower())
#문자열 양옆의 공백 제거하기 :strip()
input_a="""
      안녕하세요
문자열의 함수를 알아봅니다
"""
print(input_a)
print(input_a.strip())
#문자열 자르기 : split()
#문자열을 특정한 문자로 자를 때는 split()함수를 사용합니다. 다음과 같은 예제에서는 split 함수 괄호 안의
#문자열인 공백(띄어쓰기)을 기준을 자릅니다
a="10 20 30 40 50".split(" ")
print(a)
#실행결과로 리스트[list]가 나옵니다

#문자열 찾기 : find()와 rfind()
#문자열 내부에 특정 문자가 어디에 위치하는지 확인할 때 find()함수와 rfing()함수를 사용합니다
#find() :왼쪽부터 찾아서 처음 등장하는 위치를 찾습니다.
#rfind() : 오른쪽부터 찾아서 처음 등장하는 위치를 찾습니다
output_a="안녕하세요".find("안녕")
print(output_a)
output_b="안녕안녕하세요".rfind("안녕")
print(output_b)

#문자열과 in 연산자
#문자열 내부에 어떤 문자열이 있는지 확인하려면 in연산자를 사용합니다.
#출력은 True(맞다) 또는 False(아니다)라고 나옵니다
print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")