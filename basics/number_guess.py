# 숫자 맞추기 게임 (while + 시도 횟수)
import random

answer = random.randint(1, 100)
tries = 0
print('1~100 사이 숫자를 맞춰보세요')
while True:
    raw = input('추측: ').strip()
    try:
        guess = int(raw)
    except ValueError:
        print('정수 입력')
        continue
    tries += 1
    if guess < answer:
        print('더 큼')
    elif guess > answer:
        print('더 작음')
    else:
        print(f'정답! {tries}번 만에 성공')
        break
