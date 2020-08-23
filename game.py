'''

Copyright 2020 Dohyun Park(dhlife09) All Rights Reserved.

https://github.com/dhlife09

'''

#DEFAULT SETTING
#t = ['가위', '바위', '보']

import random   #컴퓨터(프로그램)이 랜덤으로 가위, 바위, 보 중 하나를 내기 위해 필요
import time     #시간을 Delay 시키는 용도로 사용

result = None

result_winn = '승리'
result_draw = '비겼군요'
result_lose = '패배'

#INTRO
print('\n')
print('========================================')
print('   가위바위보 게임 by Dohyun Park')
print('\n')
print(' 가위바위보 게임에 오신것을 환영합니다!')
print(' 가위(1), 바위(2), 보(3) 괄호 안에 있는')
print('        숫자를 입력해주세요!')
print('========================================')
print('\n')

#응답 대기
userInput = None
while userInput not in [ '1', '2', '3']:    #userInput 변수 값이 1, 2, 3이 아닐 경우
    userInput = input('-> ') #사용자의 입력을 변수에 저장
    if userInput == '1':
        userInputKR = '가위'
    elif userInput == '2':
     userInputKR = '보'
    elif userInput == '3':
     userInputKR = '바위'
    else:
        print('\n')
        print('========================================')
        print('   가위바위보 게임 by Dohyun Park')
        print('\n')
        print('    !!   숫자만 입력할 수 있어요   !!')
        print('       가위(1), 바위(2), 보(3) ')
        print('    가위를 낸다면 1 을 입력해 주세요')
        print('========================================')
        print('\n')
print('\n')

print('\n')
print('========================================')
print('   가위바위보 게임 by Dohyun Park')
print('\n')
print('      ', userInputKR, '를 선택했어요!')
print('     컴퓨터가 고르고 있어요!')
print('========================================')
print('\n')

time.sleep(2)
systemInput = random.randint(1, 3)  #systemInput(컴퓨터(프로그램)이 내는 값)은 랜덤 함수에 의해 1, 2, 3 셋 중 하나가 선택됨.

if systemInput == 1:
    systemInputKR = '가위'
elif systemInput == 2:
    systemInputKR = '보'
elif systemInput == 3:
    systemInputKR = '바위'
else:
    print('컴퓨터가 고르다가 오류가 발생했어요! errorResult: ', systemInput)

print('\n')
print('========================================')
print('   가위바위보 게임 by Dohyun Park')
print('\n')
print('  컴퓨터가 무엇을 낼 지 다 골랐어요! ')
print('  과연.. 누구의 승리일까요?!?!?!?!?! ')
print('========================================')
print('\n')

time.sleep(4)

if userInputKR == systemInputKR:    #userInputKR 값과 systemInputKR 값이 같을 경우 비겼을 경우임
    result = result_draw    #user가 result_draw
elif userInputKR == '가위':
    if systemInputKR == '바위': #userInputKR 값이 가위이고, systemInputKR 값이 바위일 경우
        result = result_lose    #user가 result_lose
    elif systemInputKR == '보': #userInputKR 값이 가위이고, systemInputKR 값이 보일 경우
        result = result_winn    #user가 result_winn
elif userInputKR == '바위':
    if systemInputKR == '보': #userInputKR 값이 바위이고, systemInputKR 값이 보일 경우
        result = result_lose    #user가 result_lose
    elif systemInputKR == '가위': #userInputKR 값이 바위이고, systemInputKR 값이 가위일 경우
        result = result_winn    #user가 result_winn
elif userInputKR == '보':
    if systemInputKR == '가위': #userInputKR 값이 보이고, systemInputKR 값이 가위일 경우
        result = result_lose    #user가 result_lose
    elif systemInputKR == '가위': #userInputKR 값이 보이고, systemInputKR 값이 주먹일 경우
        result = result_winn    #user가 result_winn

print('\n')
print('========================================')
print('   가위바위보 게임 by Dohyun Park')
print('\n')
print('     가위바위보 게임이 끝났습니다!')
print('         컴퓨터는', systemInputKR, '를 냈어요.')

#게임 결과
if result == result_winn:
    print('            당신의' ,result,'!')    #이겼을 때 출력되는 Message
elif result == result_lose:
    print('            당신의' ,result,'!')    #졌을 때 출력되는 Message
elif result == result_draw:
    print('              ',result,'!!')   #비겼을 때 출력되는 Message
else:
    print('     오류가 발생했어요! 83L', systemInputKR)

print('========================================')
print('\n')
