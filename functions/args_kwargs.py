"""*args, **kwargs 연습"""

def show(*items):
    for it in items:
        print('item', it)

show(1, 2, 3)
