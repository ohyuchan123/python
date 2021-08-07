#모듈
#urllib 모듈
'''
urllib모듈은 URL을 다루는 라이브러리라는 의미 입니다
'''
from urllib import request

target=request.urlopen("https://google.com")
output=target.read()

print(output)