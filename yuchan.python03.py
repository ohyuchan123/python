#반복문
#별찍기
'''
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
'''
#간단한 코드
for i in range(1, 11, 2):
    print('{:^10}'.format('*' * i))
for i in range(9, 0, -2):
    print('{:^10}'.format('*' * i))
print()
#일반 코드
for i in range(1,6):
    for j in range(5-i):
        print(' ',end="")
    for j in range(1,i*2,1):
        print('*',end="")
    print('')
for i in range(5):
    for j in range(i):
         print(' ', end="")
    for j in range(10, 1 + i * 2, -1):
        print('*', end="")
    print('')
print()
'''
*********
 *******
  *****
   ***
    *
    *
   ***
  *****
 *******
*********
'''
#간단한 코드
for i in range(9, 0, -2):
    print('{:^10}'.format('*' * i))
for i in range(3, 11, 2):
    print('{:^10}'.format('*' * i))
print()
#일반 코드
for i in range(5):
    for j in range(i):
         print(' ', end="")
    for j in range(10, 1 + i * 2, -1):
        print('*', end="")
    print('')
for i in range(1,6):
    for j in range(5-i):
        print(' ',end="")
    for j in range(1,i*2,1):
        print('*',end="")
    print('')
print()