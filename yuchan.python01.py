#함수
#with 키워드
'''
프로그램이 킬어지면  open() 함수와 close() 함수 사이에 많은 코드가 들어갑니다 조건문과 반복
문이 들어가다 보면 파일을 열고 닫지 않는 실수를 한는 경우가 생길 수 있습니다 이런 실수를 방지하기 위해
with 키워드 라는 기능이 생겼습니다
with open(문자열 : 파일 경로,문자열 : 모드) as 파일 객체:
    문장
'''
with open("basic.txt","w") as file:
    file.write("Helllo Python Programming...!")

#텍스트 읽기
'''
파일에 텍스트를 쓸 때는 방금 살펴보았던 것처럼  write() 함수를 사용합니다.
반대로 파일을 읽을 때는 read() 함수를 사용합니다
파일 객체.read()
'''
with open("basic.txt","r") as file:
    contents=file.read()
print(contents)


