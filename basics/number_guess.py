# 숫자맞추기 다시 연습 — 범위랑 문구만 바꿈
import random

answer = random.randint(1, 50)  # 어제꺼랑 비슷한데 범위만 줄임
tries = 0
print('1~50 맞춰보기')
while True:
    raw = input('숫자: ').strip()
    try:
        guess = int(raw)
    except ValueError:
        print('정수만')
        continue
    tries += 1
    if guess < answer:
        print('업')
    elif guess > answer:
        print('다운')
    else:
        print(f'맞춤! {tries}회')
        break
