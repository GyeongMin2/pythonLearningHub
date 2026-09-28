# 어제꺼랑 비슷한데 변수명이랑 출력만 바꿈
point = 91
if point >= 90:
    result = 'A'
elif point >= 80:
    result = 'B'
elif point >= 70:
    result = 'C'
elif point >= 60:
    result = 'D'
else:
    result = 'F'
print(f'{point}점이면 {result}')
if point >= 90:
    print('잘했어!')
