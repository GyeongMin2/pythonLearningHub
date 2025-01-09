# 계산기 복습 — 나누기 0만 체크 추가
a, b = 15, 0
op = '/'
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b == 0:
        print('0으로 못 나눔')
    else:
        print(a / b)
else:
    print('모르는 연산')
