#모듈
#os 모듈
'''
os모듈은 운영체제와 관련된 기능을 가진 모듈입니다 새로운 폴더를 만들거나 폴더 내부의 파일 목록을 보는
일도 모두 os 모듈을 활용해서 처리합니다
'''
import os

print("현재 운영체제 : ", os.name)
print("현재 폴더 : ",os.getcwd())
print("현재 폴더 내부의 요소 : ",os.listdir())

os.mkdir("hello")
os.rmdir("hello")

with open("original.txt","w")as file:
    file.write("hello")
os.rename("original.txt","new.txt")

os.remove("new.txt")

os.system("dir")