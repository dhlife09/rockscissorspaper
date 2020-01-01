'''

s = input('문자열을 입력하세요') #사용자의 입력을 변수에 저장
print(s)

'''

#DEFAULT SETTING
#t = ['가위', '바위', '보']

a = '가위'
b = '바위'
c = '보'

w = '이겼'
d = '비겼'
l = '졌'

#응답 대기
s = input('"가위/바위/보"중에서 무엇을 할 지 입력해주세요.\n만약 가위를 낸다면 가위 만 입력해주세요.\n입력: ') #사용자의 입력을 변수에 저장
if s == '가위':
    m = '가위'
elif s == '보':
    m = '보'
elif s == '바위':
    m = '바위'
else:
    print('정확한 값을 입력해 주세요.')

print(m, '을 선택했어요!')

#랜덤
import random
k = random.randint(1, 3)
if k == 1:
    random = '가위'
elif k == 2:
    random = '보'
elif k == 3:
    random = '바위'
else:
    print('프로그램에서 오류가 발생했어요! 42L')

print (k)

if m == k:
    result = d
elif m == a:
    if k == c:
        result = w
elif m == b:
    if k == a:
        result = w
elif m == c:
    if k == b:
        result = w
else:
    result = l


#게임 결과
print('게임이 끝났습니다! 당신은', result,'습니다!')
