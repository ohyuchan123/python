#반복문
#for 반복문 : 리스트와 범위 조합하기
array=[273,32,103,57,52]
for element in array:
    print(element)

#리스트와 범위를 조합해서 사용하기
array=[273,32,103,57,52]
for i in range(len(array)):
    print("{}번째 반복 : {}".format(i,array[i]))

#for 반복문 : 반대로 반복하기
for j in range(4,0-1,-1):
    print("현재 반복 변수 : {}".format(j))
#반대로 반복하기(2)
for k in reversed(range(5)):
    print("현재 반복 변수: {}".format(k))