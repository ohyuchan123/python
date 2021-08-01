#반복문
#별찍기
'''
*
**
***
****
*****
'''
#간단한 코드
for i in range(5):
    print('{:<5}'.format('*'*(i+1)))
#일반코드
for i in range(5):
    for j in range(i+1):
        print('*',end="")
    print('')
print()
'''
*****
****
***
**
*
'''
#간단한 코드
for i in range(6,0,-1):
    print('{:<5}'.format('*'*(i-1)))
#일반 코드
for i in range(5,0,-1):
    for j in range(i):
        print('*',end="")
    print('')
print()

'''
*****
 ****
  ***
   **
    *
'''
#간단한 코드
for i in range(6,0,-1):
    print('{:>5}'.format('*'*(i-1)))
#일반코드
for i in range(5):
    for j in range(i):
        print(' ',end="")
    for j in range(5-i):
        print('*',end="")
    print(' ')
print()

'''
    *
   **
  ***
 ****
*****
'''
#간단한 코드
for i in range(5):
    print('{:>5}'.format('*'*(i+1)))
#일반코드
for i in range(1,6):
    for j in range(5-i):
        print(' ',end="")
    for j in range(i):
        print('*',end="")
    print('')
print()