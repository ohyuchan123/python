#반복문
#enumerate() 함수와 반복문 조합하기
'''
example_list=["요소A","요소B","요소C"]
'''
#방법(1)
'''
example_list=["요소A","요소B","요소C"]
i=0
for item in example_list:
    print("{}번째 요소는{}입니다.".format(i,item))
    i+=1
'''
#방법(2)
'''
example_list=["요소A","요소B","요소C"]
for i in range(len(example_list)):
    print("{}번째 요소는 {}입니다".format(i,example_list[i])
'''
example_list=["요소A","요소B","요소C"]
print("#단순 출력")
print(example_list)
print()

print("#enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

print("#list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))