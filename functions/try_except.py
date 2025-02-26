# try / except
def parse_int(text):
    try:
        return int(text)
    except ValueError:
        print('정수 아님:', text)
        return None

print(parse_int('42'), parse_int('x'))

def read_number():
    while True:
        raw = input('숫자: ').strip()
        val = parse_int(raw)
        if val is not None:
            return val

class InputError(Exception):
    pass

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise InputError('0으로 나눔') from None

def run_safe(fn, *args):
    try:
        return fn(*args)
    except Exception as err:
        print('실패', err)
        return None

if __name__ == '__main__':
    print(run_safe(divide, 10, 2))
