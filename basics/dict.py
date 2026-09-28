# 딕셔너리 또 손봄 — get이랑 기본값만 추가
book = {'title': '파이썬', 'pages': 300, 'author': '김'}
book['year'] = 2024
for key, val in book.items():
    print(f'{key} = {val}')
print('키 개수', len(book))
print('가격?', book.get('price', '없음'))
