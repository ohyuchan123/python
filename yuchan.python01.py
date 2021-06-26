#클래스(2)
class person:
    name=""
    age=0
    job=0
    hei=0.0
    wei=0
    address=""
    phone=""
    def init(self,name,age,job,hei
             ,wei,adress,phone):
        self.name=name
        self.age=age
        self.job=job
        self.hei=hei
        self.wei=wei
        self.adress=adress
        self.phone=phone
        print("객체 생성 완료!")
길동=person()
길동.init("홍길동",20,"의적",160,15,40
        ,"서울시 강남구","010-1234-1234")

print(길동)
