# score_file=open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close

score_file=open("score.txt","r",encoding="utf8")
print(score_file.readline()) #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()