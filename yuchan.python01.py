#클래스(1)
# -객체를 정의헤 놓은것
#클래스 용도
# - 객체를 생성하는데 사용된다.

#객체
# - 실제로 존재하는 것,사물또는 개념
#객체의 용도
# - 객체의 속성과 기능에 따름
'''
클래스 : 설계도 ex) 붕어빵틀, 과자틀
객체 : 실제 물건 ex) 붕어빵,과자
'''
class Animal:
    age=0
    name=0
    def cry(self,str1):
        print(self.name,str1,"한다.")

#main
print(Animal())
a=Animal()

#id(데이터) 내장함수
print(a)
print(id(a))

#a주소를 이용해서 Animal 객체에
#토끼,3저장
a.name="토끼"
a.age=3
print(a.age)
print(a.name)

b=Animal()

b.name="강아지"
b.age=1

print(b.name)
print(b.age)

Animallist=["동물","동물2"]

Animallist.append(a)
Animallist.append(b)

print(Animallist)

#자동차 클래스
# Car
#브랜드명,가격,속력,색상

#현대 소나타
#4000
#240
#검은색

#Bens S클래스
#1억
#300
#3하얀색

class car:
    name=""
    price=0
    speed=0
    color=""
    #정보 출력 메소드
    def info(self):
        print("*"*20)
        print(self.name)
        print(self.price)
        print(self.speed)
        print(self.color)
        print("*" * 20)
Car1=car()

Car1.name="현대소나타"
Car1.price="4000"
Car1.speed="240"
Car1.color="검정색"
Car1.info()

Car2=car()

Car2.name="Bens S클래스"
Car2.price="1억"
Car2.speed="300"
Car2.color="하얀색"
Car2.info()

