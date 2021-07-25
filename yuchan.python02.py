#조건문
#elif 구문
'''
elif 구문은 if 조건문과 else 구문 사이에 입력하며, 다음과 같은 형태로 사용합니다.

if 조건A:
□ □ □ □ 조건 A가 참일때 실해할 문장
elif 조건B:
□ □ □ □ 조건 B가 참일때 실해할 문장
elif 조건C:
□ □ □ □ 조건 C가 참일때 실해할 문장
...
else :
□ □ □ □ 모든 조건이 거짓일 떄 문장
'''

#계절 구하기
#날짜/시간과 관련된 기능을 가져옵니다
import datetime

now=datetime.datetime.now()
month=now.month

#조건문으로 계절을 확인합니다
if 3<=month<=5:
    print("현재는 봄입니다")
elif 6<=month<=8:
    print("현재는 여름입니다")
elif 9<=month<=11:
    print("현재는 가을입니다")
else:
    print("현재는 겨울입니다")