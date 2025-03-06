"""함수 기본 연습"""

def add(a, b):
    return a + b

def greet(name='학생'):
    return f'안녕, {name}'

print(add(2, 3), greet())

def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

def describe(func_name):
    print('호출:', func_name)

describe('average')

def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

if __name__ == '__main__':
    print('평균', average([1, 2, 3, 4]))
    print('나눗셈', safe_div(10, 0))
