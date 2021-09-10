from random import*

wether=int(random()*3+1)
print("(1) : 비 (2) : 미세먼지 (3) : 맑아요")
print(wether)
if wether==1:
    print("우산을 챙기세요")
elif wether==2:
    print("마스크를 챙기세요")
elif wether==3:
    print("준비물이 필요 없어요")
