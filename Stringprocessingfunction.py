python="Python is Amazing"
#모든 문자를 소문자로
print(python.lower())
#모든 문자를 대문자로
print(python.upper())
#문장의 첫번째 값을 대문자인지 구별해줌
print(python[0].isupper())
#문자의 길이
print(len(python))
#문자를 바꾸어 줌
print(python.replace("Python","java"))

#문장에 n이 몇번째에 위치하는 지 알려줌
index=python.index("n")
print(index)
#문자의 두번째 n의 위치한 곳을 출력
index=python.index("n",index+1)
print(index)

print(python.find("n"))
