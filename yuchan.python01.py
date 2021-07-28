#반복문
#리스트에 요소 추가하기 : append,insert
'''
리스트명.append(요소)
리스터명.insert(위치,요소)
'''
list_a=[1,2,3]

print("#리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()
print("#리스트 중간에 요소 추가하기")
list_a.insert(0,10)
print(list_a)