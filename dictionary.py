cabinet={3:"유재석",100:"김태호"}
#값을 가져옴
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# 값이 없을때 그냥 받으면 hi까지 출력이 되지 않는다
#print(cabinet[5])
#값이 없을때 get으로 받으면 hi까지 출력되고
print(cabinet.get(5))
print(cabinet.get(5,"사용 가능"))
print("hi")