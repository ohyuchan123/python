#클래스-생성자
#놀이동산 50%
#영화 몇회 무료
#쇼핑 30%
#교통카드
class Trans_Card:
    pass #교통카드
class Shopping:
    pass #쇼핑
class Movie:
    pass #영화
class Card:
    def __init__(self,name,pw,number):
        self.name=name
        self.pw=pw
        self.number=number
        print("카드생성완료")
    def pay(self):
        print("결제합니다")
#다중 상속
#클래스들끼리 여러개를 상속 받을 수 있다.
#class 클래스명(상.클1,상.클2.....)
#삼성카드->쇼핑,쿄통
class Samsung_Card(Card,Shopping,Trans_Card):
    pass
#롯데카드->영화
class Lotte_Card(Card,Movie):
    pass
#kb카드->결제
class Kb_Card(Card):
    pass
