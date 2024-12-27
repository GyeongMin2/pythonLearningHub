# 딕셔너리 또 연습 — items() 출력 문구만 바꿈
book = {'title': '파이썬', 'pages': 300, 'author': '김'}
book['year'] = 2024
for key, val in book.items():
    print(f'{key} = {val}')
print('키 개수', len(book))
