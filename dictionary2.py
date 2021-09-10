cabinet={3:"유재석",100:"김태호"}

#키가 있는 지 확인 할 수 있음
print(3 in cabinet)
print(5 in cabinet)

cabinet={"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"]="김종국"
cabinet["C-20"]="조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key,value 쌍으로 출력
print(cabinet.items())

#목욕탕 패점
cabinet.clear()
print(cabinet)