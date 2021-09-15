score_file=open("score.txt","r",encoding="utf8")
while True:
    line=score_file.readline()
    if not line:
        break
    print(line)
score_file.close()