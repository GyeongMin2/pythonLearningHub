# 자료형 복습 — try 변환만 추가
samples = [0, 2.5, '글자', (1, 2), {'a': 1}]
for item in samples:
    print(item, '타입:', type(item).__name__)
text = '42'
try:
    print('정수 OK', int(text))
except ValueError:
    print('변환 실패')
