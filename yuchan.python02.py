#함수
#제네레이터
def test():
    print("함수가 호출되었습니다.")
    yield "test"

print("A 지점 통과")
test()

print("B 지점 통과")
test()
print(test())
