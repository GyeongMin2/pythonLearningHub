"""*args, **kwargs 연습"""

def show(*items):
    for it in items:
        print('item', it)

show(1, 2, 3)

def profile(**info):
    for k, v in info.items():
        print(k, v)

profile(name='민수', age=21)

def mix(a, b=0, *args, **kwargs):
    print('a,b', a, b)
    print('args', args)
    print('kwargs', kwargs)

def total_price(base, *extras, discount=0):
    s = base + sum(extras)
    return s - discount

if __name__ == '__main__':
    print(total_price(1000, 200, 300, discount=100))

# 복습: 가변 인자 정리
def log_call(fn_name, *a, **kw):
    print(fn_name, a, kw)
