#함수
#변수의 값을 교환하는 튜플
a,b=10,20
print("#교환 전 값")
print("a : ",a)
print("b : ",b)
print()

#값을 교환합니다
a,b=b,a

print("#교환 후 값")
print("a : ",a)
print("b : ",b)
print()

#튜플 과 함수
def test():
    return (10,20)
a,b=test()

print("a : ",a)
print("b : ",b)


