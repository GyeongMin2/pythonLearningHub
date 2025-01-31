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
