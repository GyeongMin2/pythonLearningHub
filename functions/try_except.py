# try / except
def parse_int(text):
    try:
        return int(text)
    except ValueError:
        print('정수 아님:', text)
        return None

print(parse_int('42'), parse_int('x'))
