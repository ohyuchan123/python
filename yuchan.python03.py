#sys 모듈
'''
sys 모듈은 시스템과 관련된 정보를 가지고 있는 모듈입니다.
'''
import sys

#명령 매개변수를 출력합니다
print(sys.argv)
print("---")

#컴퓨터 환경과 관련된 정보를 출ㄹ력합니다
print("getwindowsversion : ()",sys.getwindowsversion())
print("---")
print("copyright : ",sys.copyright)
print("---")
print("version : ",sys.version)

#프로그램을 강제로 종료합니다
sys.exit()