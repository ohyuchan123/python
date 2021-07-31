#반복문
#while 반복문 : break 키워드/continue 키워드
i=0
while True:
    print("{}번째 반복문입니다.".format(i))
    i+=1
    input_text=input(">종료하시겠습니까?(y/n) : ")
    if input_text in["y","Y"]:
        print("반복을 종료합니다.")
        break
    elif input_text in["n","N"]:
        print("반복을 계속합니다")

#continue 키워드
numbers=[5,15,6,20,7,25]

for number in numbers:
    if number<10:
        continue
    print(number)