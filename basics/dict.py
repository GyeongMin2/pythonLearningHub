# 딕셔너리 다시 연습 — 어제꺼랑 비슷한데 키만 바꿈
person = {'name': '영희', 'age': 21, 'major': '통계'}
person['grade'] = 'A'
person['city'] = '서울'
for k, v in person.items():
    print(k, ':', v)
