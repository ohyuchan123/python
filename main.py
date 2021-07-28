#반복문
#리스트에 요소 제거하기
#인덱스로 제거하기 : del,pop
list_a=[0,1,2,3,4,5]
print("#리스트의 요소 하나 제거하기")

#제거 방법[1]-del
del list_a[1]
print("del list_a[1] : ",list_a)

#제거 방법[2]-pop
list_a.pop(2)
print("pop(2) : ",list_a)

#값으로 제거하기 :remove
'''
리스트.remove(값)
'''
list_c=[1,2,1,2]
list_c.remove(2)
print(list_c)
#모두 제거하기 : clear
'''
리스트.clear()
'''
list_d=[0,1,2,3,4,5]
list_d.clear()
print(list_d)