#반복문
'''
리스트 기호인 대괄호[] 안에 들어간 숫자를 인덱스(index)라고 부릅니다.
'''

list_a=[273,32,103,"문자열",True,False]
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[1:3])

list_a[0]="변경"
print(list_a[0])

#첫째 대괄호 안에 음수를 넣어 뒤에서부터 요소를 선택할 수 있습니다
print(list_a[-1])
print(list_a[-2])
print(list_a[-3])
#둘째 리스트 접근 연산자를 다음과 같이 이주으로 사용할 수 있습니다
print(list_a[3])
print(list_a[3][0])
#셋째 리스트 안에 리스트를 사용할 수 도 있습니다
list_b=[[1,2,3],[4,5,6],[7,8,9]]
print(list_b[1])
print(list_b[1][1])