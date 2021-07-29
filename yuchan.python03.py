#반복문
#for반복문  : 딕셔너리와 함께 사용함
dictionary={
    "name":"7D 건조 망고",
    "type":"당절임",
    "ingredient":["망고","설탕","메타중아환산나트륨","치자황색소"],
    "origin":"필리핀"
}
#for 반복문을 사용합니다
for key in dictionary:
    print(key,":",dictionary[key])