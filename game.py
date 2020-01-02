'''

s = input('문자열을 입력하세요') #사용자의 입력을 변수에 저장
print(s)

'''

#DEFAULT SETTING
#t = ['가위', '바위', '보']

a = '가위'
b = '바위'
c = '보'

w = '승리'
d = '비겼군요'
l = '패배'

#INTRO
print('\n')
print(' ==========')
print(' 가위바위보 게임')
print(' Made by dhlife09')
print(' (github.com/dhlife09)')
print(' ==========')
print('\n')

#응답 대기
s = None
while s not in [ '가위', '바위', '보']:
    s = input(' "가위/바위/보" 중에 무엇을 낼까요? >> ') #사용자의 입력을 변수에 저장
    if s == '가위':
        m = '가위'
    elif s == '보':
     m = '보'
    elif s == '바위':
     m = '바위'
    else:
        print(' "가위/바위/보" 중 낼 것 만 입력해 주세요! (예시: 가위를 낸다면 "가위" 만 입력.)')
print('\n')
print(' ', m, '를 선택했어요!')

#랜덤
import random
k = random.randint(1, 3)
if k == 1:
    i = '가위'
elif k == 2:
    i = '보'
elif k == 3:
    i = '바위'
else:
    print(' 프로그램에서 오류가 발생했어요! 53L')


if m == i:
    result = d
elif m == a:
    if i == c:
        result = w
    else:
        result = l
elif m == b:
    if i == a:
        result = w
    else:
        result = l
elif m == c:
    if i == b:
        result = w
    else:
        result = l

print('\n') #게임 결과 출력 전 공백

#게임 결과
if result == w:
    print(' 게임이 끝났습니다! 컴퓨터는', i,'를 냈어요. 당신의' ,result,'!')
elif result == l:
    print(' 게임이 끝났습니다! 컴퓨터는', i,'를 냈어요. 당신의' ,result,'!')
elif result == d:
    print(' 게임이 끝났습니다! 컴퓨터는', i,'를 냈어요.' ,result,'!')
else:
    print(' 오류가 발생했어요! 83L')

print('\n') #게임 종료
print('\n') #게임 종료
