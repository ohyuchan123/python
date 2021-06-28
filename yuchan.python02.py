#클래스-생성자
#교수,어린이,학생
#->사람->먹고 놀고 자고 기능
#기본클래스(부모클래스)
class Person:
    def __init__(self,name,age,job):
        self.name=name
        self.age=age
        self.job=job
    def eat(self):
        print(self.name+"님이 먹는다/.")
    def sleep(self):
        print(self.name+"님이 잔다/.")
    def play(self):
        print(self.name+"님이 논다/.")
    def __del__(self):
        print("객체가 소멸합니다/.")
class Child(Person):
    pass
class Student(Person):
    pass
class professor(Person):
    pass
