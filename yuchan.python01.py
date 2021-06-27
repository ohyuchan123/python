#클래스(3)
#class A:
    #빈클래스
    #기본생성자
    #def _init_(self):
        #print("A")
    #pass
#A()
class Account:
    def _init_(self,name,num,money,pw):
        self.acc_name = name
        self.acc_num = num
        self.acc_balance = money
        self.acc_pw = pw
        print("계좌 등록ok")
    def with1(self,money):
        if money<=self.acc_balance:
            self.acc_balance-=money
            return money
        else:
            return "잔액부족"
    def posit(self,money):
        self.acc_balance+=money
        print("입금액:",money)

영희=Account("영희계좌","1111",1000,1234)
print(영희.acc_name)
영희.posit(20000 )
print("출금:",영희.with1(50000))