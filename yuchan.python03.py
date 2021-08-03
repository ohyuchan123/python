#함수
#파일 처리
'''
파일과 관련된 처리를 하는 함수는 표준 함수가 기본으로 제공된다
파일은 크게 텍스트 파일과 바이너리 파일로 나뉜다

파일 열고 닫기
open()
파일 객체 = open(문자열 : 파일경로,문자열 : 읽기모드)
w : wrtie 모드(새로 쓰기 모드)
a : apeend 모드(뒤에 이어서 쓰기 모드)
r : read 모드(읽기 모드)

파일 객체.close()
'''
file=open("basic.txt","w")
file.write("Helllo Python Programming...!")
file.close()



