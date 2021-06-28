#클래스-생성자
#기본 캐릭터
class Character:
    def __init__(self,id1="무명시",hp=0,mp=0):
        self.id1=id1 #id
        self.hp=hp   #체력
        self.mp=mp   #마법력
    def info(self):
        print("id>",self.id1)
        print("hp>", self.hp)
        print("mp>", self.mp)
    def at(self):
        print("기본공격")
#전사
class Warrior(Character):
    pass
#마법사
class Wizard(Character):
    pass
#궁수(화살)
class Archer(Character):
    pass
class Monster(Character):
    pass
#전사
w1=Warrior("전사")
print(w1.at())

m1=Monster("오크",100,100)
print(m1.info())