# 자료형 다시 연습 — 샘플만 바꿈
samples = [0, 2.5, '글자', (1, 2), {'a': 1}]
for item in samples:
    print(item, '타입:', type(item).__name__)
print('변환', int('42') + 1)
