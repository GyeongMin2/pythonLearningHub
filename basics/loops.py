# for / while 복습 — 주석만 달아둠
for i in range(1, 6):
    print('*' * i)

n = 0
while n < 10:
    print('while', n)
    n += 1
    if n >= 4:  # 4에서 끊기
        break
