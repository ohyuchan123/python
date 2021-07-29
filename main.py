#반복문
#딕셔너리와 반복문
#딕셔너리 선언하기
'''
딕셔너리는 중괄호{}로 선언하며, '키:값' 형태를 쉼표(,)로 연결해서 만듭니다. 키는 문자열,숫자,불 등으로 선언할 수 있습니다
변수={
    키:값
    키:값
    ...
    키:값
'''
dict_a={
    "name":"어밴져스 엔드게임",
    "type":"히어로 무비"
}

print(dict_a)
print(dict_a["name"])
print(dict_a["type"])

dict_b={
    "director":["안소니 루소","조 루소"],
    "cast":["아이언맨","타노스","토르","닥터스트레인지","헐크"]
}
print(dict_b)
print(dict_b["director"])