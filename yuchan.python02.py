#함수
#filter()함수와 map()함수
'''
함수를 매개변수로 전달하는 대표적인 표준함수로 map() 함수와 filter()함수가 있다
map() : map(함수,리스트)
filter() : filter(함수,리스트)
'''
def power(item):
    return item*item
def under_3(item):
    return item<3

list_input_a=[1,2,3,4,5]

#map() 함수 사용
output_a=map(power,list_input_a)
print("# map() 함수의 실행결과")
print("map(power,list_input_a) : ",output_a)
print("map(power,list_input_a) : ",list(output_a))

#filter() 함수 사용
output_b=filter(under_3,list_input_a)
print("# filter() 함수의 실행결과")
print("filter(under_3,list_input_a) : ",output_b)
print("filter(under_3,list_input_a) : ",list(output_b))

