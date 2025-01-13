# 문자열 또 연습 — split/join만 살짝
s = '  Hello Python  '
print(s.strip())
print(s.lower(), s.upper())
print(s.replace('Python', '파이썬'))
parts = 'a,b,c'.split(',')
print('split', parts)
print('join', '-'.join(parts))
