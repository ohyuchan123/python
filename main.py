#클래스 생성자
#평균클래스
#평균을 내는 기능

#총점 클래스
#총점을 저장하는 변수
#총점을 계산하는 기능

class Avg:
    def __init__(self):
        self.avg=0
    def average(self,total):
        self.avg=self.total/3
        print("평균<",self.avg)
class Total(Avg):
    def total(self,kor,math,eng):
        self.kor=kor
        self.math=math
        self.eng=eng
        self.total=kor+math+eng
        self.average(self.total)

person1=Total()
print(person1.total(92,92,92))