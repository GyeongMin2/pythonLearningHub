# for 다시 연습 — range랑 break 조건만 바꿈
for i in range(1, 6):
    print('*' * i)

n = 0
while n < 10:
    print('while', n)
    n += 1
    if n >= 4:
        break
