#클래스(3)
class Tv:
    brand_name=""
    color=""
    power=False
    channel=10
    def init(self,color,power,channel,name):
        self.name=name
        self.color=color
        self.channel=channel
        print("Tv")
    def power(self,power):
        not power
    def channelUp(self,channel):
        channel+=1
    def channeldown(self,channel):
        channel-=1
samsung=Tv()
print(samsung.init("하얀색",2,"삼성Tv"))

lg=Tv()
print(lg.init("하얀색",5,"lGTv"))
