# 조건문 연습 2 — if_else랑 거의 같은 구조
temp = 18
if temp >= 30:
    weather = '더움'
elif temp >= 20:
    weather = '따뜻'
elif temp >= 10:
    weather = '쌀쌀'
else:
    weather = '추움'
print('날씨:', weather)
