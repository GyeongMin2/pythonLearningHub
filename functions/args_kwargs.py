"""*args, **kwargs 연습"""

def show(*items):
    for it in items:
        print('item', it)

show(1, 2, 3)

def profile(**info):
    for k, v in info.items():
        print(k, v)

profile(name='민수', age=21)
