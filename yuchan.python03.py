#반복문
#해당하는 값 모두 제거하기
list_test=[1,2,1,2]
value=2

while value in list_test:
    list_test.remove(value)

print(list_test)