#!/usr/bin/env python3
"""Generate enriched commit_history.json from schedule skeleton."""

from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKELETON = Path("/tmp/ref_history.json")
OUT = REPO / "commit_history.json"


def nl(*lines: str) -> str:
    return "\n".join(lines) + "\n"


BUILDERS: dict[str, callable] = {}


def register(path: str):
    def deco(fn):
        BUILDERS[path] = fn
        return fn

    return deco


# --- basics ---


@register("basics/hello.py")
def basics_hello(rev: int, _total: int) -> str:
    lines = [
        "# 파이썬 첫 출력 — 6개월 공부 시작",
        "name = '학생'",
        "goal = '기초부터 차근차근'",
        "print('Hello', name)",
        "print('목표:', goal)",
    ]
    if rev >= 2:
        lines += [
            "",
            "def greet(who: str) -> None:",
            "    print(f'안녕, {who}!')",
            "",
            "greet(name)",
        ]
    if rev >= 3:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    # 디버깅용",
            "    print('메인에서 실행')",
            "    greet('파이썬')",
        ]
    if rev >= 4:
        lines += [
            "",
            "notes = ['변수', '출력', '함수']",
            "for i, topic in enumerate(notes, 1):",
            "    print(i, topic)",
        ]
    return nl(*lines)


@register("basics/variables.py")
def basics_variables(rev: int, _total: int) -> str:
    lines = [
        "# 변수와 기본 연산",
        "a = 10",
        "b = 3.5",
        "c = 'hello'",
        "d = True",
        "print(a, b, c, d)",
        "print('합:', a + int(b))",
    ]
    if rev >= 2:
        lines += [
            "",
            "print(type(a), type(b), type(c), type(d))",
            "pi = 3.14159",
            "print('pi 반올림', round(pi, 2))",
        ]
    if rev >= 3:
        lines += [
            "",
            "# 변수 교환",
            "x, y = 5, 10",
            "x, y = y, x",
            "print('swap', x, y)",
            "print('곱', x * y)",
        ]
    if rev >= 4:
        lines += [
            "",
            "def swap(a_val, b_val):",
            "    return b_val, a_val",
            "",
            "m, n = 1, 2",
            "m, n = swap(m, n)",
            "print('함수 swap', m, n)",
        ]
    return nl(*lines)


@register("basics/types.py")
def basics_types(rev: int, _total: int) -> str:
    lines = [
        "# 자료형 확인",
        "samples = [10, 3.14, '문자', [1, 2, 3], {'k': 1}]",
        "for item in samples:",
        "    print(item, '->', type(item).__name__)",
    ]
    if rev >= 2:
        lines += [
            "",
            "n = '123'",
            "print('int 변환', int(n) + 7)",
            "print('str 붙이기', str(100) + '점')",
            "print('float', float('3.14'))",
        ]
    if rev >= 3:
        lines += [
            "",
            "text = '42'",
            "try:",
            "    num = int(text)",
            "    print('정수 OK', num)",
            "except ValueError as err:",
            "    print('변환 실패', err)",
        ]
    return nl(*lines)


@register("basics/if_else.py")
def basics_if_else(rev: int, _total: int) -> str:
    lines = [
        "# if-elif-else 연습",
        "score = 85",
        "if score >= 90:",
        "    grade = 'A'",
        "elif score >= 80:",
        "    grade = 'B'",
        "elif score >= 70:",
        "    grade = 'C'",
        "else:",
        "    grade = 'F'",
        "print('등급:', grade)",
    ]
    if rev >= 2:
        lines = [
            "# 성적 판정 (입력)",
            "raw = input('점수 입력: ').strip()",
            "try:",
            "    score = int(raw)",
            "except ValueError:",
            "    print('숫자로 입력해주세요')",
            "    score = 0",
            "if score >= 90:",
            "    grade = 'A'",
            "elif score >= 80:",
            "    grade = 'B'",
            "elif score >= 70:",
            "    grade = 'C'",
            "elif score >= 60:",
            "    grade = 'D'",
            "else:",
            "    grade = 'F'",
            "print(f'점수 {score} -> {grade}')",
        ]
    if rev >= 3:
        lines += [
            "",
            "def letter_grade(point: int) -> str:",
            "    if point >= 90:",
            "        return 'A'",
            "    if point >= 80:",
            "        return 'B'",
            "    if point >= 70:",
            "        return 'C'",
            "    if point >= 60:",
            "        return 'D'",
            "    return 'F'",
            "",
            "print('함수 테스트', letter_grade(88))",
        ]
    return nl(*lines)


@register("basics/loops.py")
def basics_loops(rev: int, _total: int) -> str:
    lines = [
        "# for / while 기본",
        "for i in range(1, 6):",
        "    print('*' * i)",
        "",
        "n = 0",
        "while n < 3:",
        "    print('while', n)",
        "    n += 1",
    ]
    if rev >= 2:
        lines = [
            "# 구구단 2~9",
            "for i in range(2, 10):",
            "    for j in range(1, 10):",
            "        print(f'{i}x{j}={i*j}', end='  ')",
            "    print()",
        ]
    if rev >= 3:
        lines += [
            "",
            "# break / continue",
            "total = 0",
            "for i in range(1, 101):",
            "    if i % 2 == 0:",
            "        continue",
            "    total += i",
            "    if total > 500:",
            "        break",
            "print('홀수 합(제한):', total)",
        ]
    return nl(*lines)


@register("basics/lists.py")
def basics_lists(rev: int, _total: int) -> str:
    lines = [
        "# 리스트 기본",
        "nums = [3, 1, 4, 1, 5, 9]",
        "print('첫값', nums[0], '길이', len(nums))",
        "nums.append(2)",
        "print('append', nums)",
    ]
    if rev >= 2:
        lines += [
            "",
            "nums.sort()",
            "print('정렬', nums)",
            "print('1 개수', nums.count(1))",
        ]
    if rev >= 3:
        lines += [
            "",
            "squares = [i * i for i in range(1, 11)]",
            "evens = [i for i in range(20) if i % 2 == 0]",
            "print('squares', squares[:5], '...')",
            "print('evens', evens[:8], '...')",
        ]
    return nl(*lines)


@register("basics/strings.py")
def basics_strings(rev: int, _total: int) -> str:
    lines = [
        "# 문자열 인덱싱/메서드",
        "s = '  Python Study  '",
        "print(s.strip())",
        "print(s.lower(), s.upper())",
        "print(s.replace('Study', '공부'))",
    ]
    if rev >= 2:
        lines += [
            "",
            "text = '  hello world  '",
            "print(text.strip())",
            "print('split', 'a,b,c'.split(','))",
            "print('join', '-'.join(['a', 'b', 'c']))",
        ]
    if rev >= 3:
        lines += [
            "",
            "name, age = '민수', 20",
            "print(f'{name}은 {age}살')",
            "print('{:.2f}'.format(3.14159))",
        ]
    return nl(*lines)


@register("basics/dict.py")
def basics_dict(rev: int, _total: int) -> str:
    lines = [
        "# 딕셔너리",
        "student = {'name': '철수', 'age': 20, 'major': '컴공'}",
        "student['grade'] = 'B'",
        "for key, val in student.items():",
        "    print(key, '=>', val)",
    ]
    if rev >= 2:
        lines = [
            "# 단어 빈도 (수동)",
            "words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']",
            "freq: dict[str, int] = {}",
            "for w in words:",
            "    freq[w] = freq.get(w, 0) + 1",
            "print(freq)",
        ]
    if rev >= 3:
        lines = [
            "# Counter 사용",
            "from collections import Counter",
            "",
            "words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']",
            "counts = Counter(words)",
            "print(counts)",
            "print('most common', counts.most_common(2))",
        ]
    if rev >= 4:
        lines += [
            "",
            "def top_word(items: list[str]) -> str:",
            "    c = Counter(items)",
            "    return c.most_common(1)[0][0]",
            "",
            "print('top', top_word(words))",
        ]
    return nl(*lines)


@register("basics/practice_calc.py")
def basics_practice_calc(rev: int, _total: int) -> str:
    lines = [
        "# 간단 계산기",
        "a, b = 10, 3",
        "print('+, -, *, /', a + b, a - b, a * b, a / b)",
    ]
    if rev >= 2:
        lines = [
            "# 입력 계산기",
            "a = float(input('첫 번째 수: '))",
            "b = float(input('두 번째 수: '))",
            "op = input('연산 (+,-,*,/): ').strip()",
            "if op == '+':",
            "    print(a + b)",
            "elif op == '-':",
            "    print(a - b)",
            "elif op == '*':",
            "    print(a * b)",
            "elif op == '/':",
            "    print(a / b)",
            "else:",
            "    print('모르는 연산자')",
        ]
    if rev >= 3:
        lines = [
            "# 계산기 + 0 나누기 처리",
            "def calc(x: float, y: float, op: str):",
            "    if op == '+':",
            "        return x + y",
            "    if op == '-':",
            "        return x - y",
            "    if op == '*':",
            "        return x * y",
            "    if op == '/':",
            "        if y == 0:",
            "            raise ZeroDivisionError('0으로 나눌 수 없음')",
            "        return x / y",
            "    raise ValueError('연산자 오류')",
            "",
            "if __name__ == '__main__':",
            "    a = float(input('첫 번째 수: '))",
            "    b = float(input('두 번째 수: '))",
            "    op = input('연산: ').strip()",
            "    try:",
            "        print('결과', calc(a, b, op))",
            "    except (ValueError, ZeroDivisionError) as e:",
            "        print('에러', e)",
        ]
    return nl(*lines)


@register("basics/number_guess.py")
def basics_number_guess(rev: int, _total: int) -> str:
    return nl(
        "# 숫자 맞추기 게임 (while + 시도 횟수)",
        "import random",
        "",
        "def play():",
        "    answer = random.randint(1, 100)",
        "    tries = 0",
        "    print('1~100 사이 숫자를 맞춰보세요')",
        "    while True:",
        "        raw = input('추측: ').strip()",
        "        try:",
        "            guess = int(raw)",
        "        except ValueError:",
        "            print('정수 입력')",
        "            continue",
        "        tries += 1",
        "        if guess < answer:",
        "            print('더 큼')",
        "        elif guess > answer:",
        "            print('더 작음')",
        "        else:",
        "            print(f'정답! {tries}번 만에 성공')",
        "            break",
        "",
        "if __name__ == '__main__':",
        "    play()",
    )


# --- functions ---


@register("functions/basic_func.py")
def functions_basic_func(rev: int, _total: int) -> str:
    lines = [
        '"""함수 기본 연습"""',
        "",
        "def add(a, b):",
        "    return a + b",
        "",
        "def greet(name='학생'):",
        "    return f'안녕, {name}'",
        "",
        "print(add(2, 3), greet())",
    ]
    if rev >= 2:
        lines += [
            "",
            "def average(nums):",
            "    if not nums:",
            "        return 0",
            "    return sum(nums) / len(nums)",
        ]
    if rev >= 3:
        lines += [
            "",
            "def describe(func_name):",
            "    print('호출:', func_name)",
            "",
            "describe('average')",
        ]
    if rev >= 4:
        lines += [
            "",
            "def safe_div(a, b):",
            "    try:",
            "        return a / b",
            "    except ZeroDivisionError:",
            "        return None",
        ]
    if rev >= 5:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    print('평균', average([1, 2, 3, 4]))",
            "    print('나눗셈', safe_div(10, 0))",
        ]
    return nl(*lines)


@register("functions/args_kwargs.py")
def functions_args_kwargs(rev: int, _total: int) -> str:
    lines = [
        '"""*args, **kwargs 연습"""',
        "",
        "def show(*items):",
        "    for it in items:",
        "        print('item', it)",
        "",
        "show(1, 2, 3)",
    ]
    if rev >= 2:
        lines += [
            "",
            "def profile(**info):",
            "    for k, v in info.items():",
            "        print(k, v)",
            "",
            "profile(name='민수', age=21)",
        ]
    if rev >= 3:
        lines += [
            "",
            "def mix(a, b=0, *args, **kwargs):",
            "    print('a,b', a, b)",
            "    print('args', args)",
            "    print('kwargs', kwargs)",
        ]
    if rev >= 4:
        lines += [
            "",
            "def total_price(base, *extras, discount=0):",
            "    s = base + sum(extras)",
            "    return s - discount",
        ]
    if rev >= 5:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    print(total_price(1000, 200, 300, discount=100))",
        ]
    if rev >= 6:
        lines += [
            "",
            "# 복습: 가변 인자 정리",
            "def log_call(fn_name, *a, **kw):",
            "    print(fn_name, a, kw)",
        ]
    return nl(*lines)


@register("functions/lambda_map.py")
def functions_lambda_map(rev: int, _total: int) -> str:
    lines = [
        "# lambda, map, filter",
        "nums = [1, 2, 3, 4, 5]",
        "squares = list(map(lambda x: x * x, nums))",
        "evens = list(filter(lambda x: x % 2 == 0, nums))",
        "print(squares, evens)",
    ]
    if rev >= 2:
        lines += [
            "",
            "names = ['kim', 'lee', 'park']",
            "upper = list(map(str.upper, names))",
            "print(upper)",
        ]
    if rev >= 3:
        lines += [
            "",
            "pairs = [(1, 'a'), (2, 'b')]",
            "by_num = sorted(pairs, key=lambda p: p[0])",
            "print(by_num)",
        ]
    if rev >= 4:
        lines += [
            "",
            "def apply_twice(fn, value):",
            "    return fn(fn(value))",
            "",
            "print(apply_twice(lambda x: x + 1, 3))",
        ]
    return nl(*lines)


@register("functions/recursion.py")
def functions_recursion(rev: int, _total: int) -> str:
    lines = [
        "# 재귀 함수",
        "def factorial(n):",
        "    if n <= 1:",
        "        return 1",
        "    return n * factorial(n - 1)",
        "",
        "print(factorial(5))",
    ]
    if rev >= 2:
        lines += [
            "",
            "def fib(n):",
            "    if n <= 1:",
            "        return n",
            "    return fib(n - 1) + fib(n - 2)",
        ]
    if rev >= 3:
        lines = lines[:8] + [
            "",
            "def fib(n, memo=None):",
            "    if memo is None:",
            "        memo = {}",
            "    if n in memo:",
            "        return memo[n]",
            "    if n <= 1:",
            "        return n",
            "    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)",
            "    return memo[n]",
            "",
            "print('fib 10', fib(10))",
        ]
    if rev >= 4:
        lines += [
            "",
            "def countdown(n):",
            "    if n <= 0:",
            "        print('끝')",
            "        return",
            "    print(n)",
            "    countdown(n - 1)",
        ]
    if rev >= 5:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    print('fact', factorial(6))",
        ]
    return nl(*lines)


@register("functions/try_except.py")
def functions_try_except(rev: int, _total: int) -> str:
    lines = [
        "# try / except",
        "def parse_int(text):",
        "    try:",
        "        return int(text)",
        "    except ValueError:",
        "        print('정수 아님:', text)",
        "        return None",
        "",
        "print(parse_int('42'), parse_int('x'))",
    ]
    if rev >= 2:
        lines += [
            "",
            "def read_number():",
            "    while True:",
            "        raw = input('숫자: ').strip()",
            "        val = parse_int(raw)",
            "        if val is not None:",
            "            return val",
        ]
    if rev >= 3:
        lines += [
            "",
            "class InputError(Exception):",
            "    pass",
        ]
    if rev >= 4:
        lines += [
            "",
            "def divide(a, b):",
            "    try:",
            "        return a / b",
            "    except ZeroDivisionError:",
            "        raise InputError('0으로 나눔') from None",
        ]
    if rev >= 5:
        lines += [
            "",
            "def run_safe(fn, *args):",
            "    try:",
            "        return fn(*args)",
            "    except Exception as err:",
            "        print('실패', err)",
            "        return None",
        ]
    if rev >= 6:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    print(run_safe(divide, 10, 2))",
        ]
    if rev >= 7:
        lines += [
            "",
            "# finally 예제",
            "def demo_finally():",
            "    try:",
            "        print('work')",
            "    finally:",
            "        print('cleanup')",
        ]
    return nl(*lines)


@register("functions/utils.py")
def functions_utils(rev: int, _total: int) -> str:
    lines = [
        '"""자주 쓰는 유틸 함수 모음"""',
        "",
        "def is_even(n: int) -> bool:",
        "    return n % 2 == 0",
        "",
        "def clamp(n, lo, hi):",
        "    return max(lo, min(hi, n))",
    ]
    if rev >= 2:
        lines += [
            "",
            "def average(nums):",
            "    if not nums:",
            "        raise ValueError('빈 리스트')",
            "    return sum(nums) / len(nums)",
        ]
    if rev >= 3:
        lines += [
            "",
            "def unique(seq):",
            "    seen = []",
            "    for x in seq:",
            "        if x not in seen:",
            "            seen.append(x)",
            "    return seen",
        ]
    if rev >= 4:
        lines += [
            "",
            "def read_lines(path):",
            "    try:",
            "        with open(path, encoding='utf-8') as f:",
            "            return f.read().splitlines()",
            "    except FileNotFoundError:",
            "        return []",
        ]
    if rev >= 5:
        lines += [
            "",
            "def slugify(text: str) -> str:",
            "    return text.strip().lower().replace(' ', '-')",
        ]
    if rev >= 6:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    print(average([1, 2, 3]))",
            "    print(unique([1, 1, 2, 3, 2]))",
            f"    # 복습 메모 rev {rev}",
        ]
    return nl(*lines)


@register("functions/modules_demo.py")
def functions_modules_demo(rev: int, _total: int) -> str:
    lines = [
        '"""모듈 import 연습"""',
        "import math",
        "from datetime import date",
        "",
        "print('pi', round(math.pi, 4))",
        "print('오늘', date.today())",
    ]
    if rev >= 2:
        lines += [
            "",
            "import random",
            "print('주사위', random.randint(1, 6))",
        ]
    if rev >= 3:
        lines += [
            "",
            "from pathlib import Path",
            "here = Path(__file__).resolve().parent",
            "print('경로', here)",
        ]
    if rev >= 4:
        lines += [
            "",
            "def circle_area(r):",
            "    return math.pi * r * r",
        ]
    if rev >= 5:
        lines += [
            "",
            "import json",
            "sample = {'topic': 'modules', 'ok': True}",
            "print(json.dumps(sample, ensure_ascii=False))",
        ]
    if rev >= 6:
        lines += [
            "",
            "def demo():",
            "    print('demo', circle_area(3))",
        ]
    if rev >= 7:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    demo()",
            "    # 가독성 개선 메모",
        ]
    return nl(*lines)


# --- oop ---


@register("oop/animal.py")
def oop_animal(rev: int, _total: int) -> str:
    lines = [
        "# 상속 예제 — 동물",
        "class Animal:",
        "    def __init__(self, name):",
        "        self.name = name",
        "",
        "    def speak(self):",
        "        return '...'",
        "",
        "class Dog(Animal):",
        "    def speak(self):",
        "        return '멍멍'",
    ]
    if rev >= 2:
        lines += [
            "",
            "class Cat(Animal):",
            "    def speak(self):",
            "        return '야옹'",
        ]
    if rev >= 3:
        lines += [
            "",
            "def introduce(pet: Animal):",
            "    print(pet.name, pet.speak())",
            "",
            "if __name__ == '__main__':",
            "    introduce(Dog('바둑'))",
            "    introduce(Cat('나비'))",
        ]
    return nl(*lines)


@register("oop/student.py")
def oop_student(rev: int, _total: int) -> str:
    lines = [
        "class Student:",
        "    def __init__(self, name, student_id):",
        "        self.name = name",
        "        self.student_id = student_id",
        "        self.scores = []",
        "",
        "    def add_score(self, score):",
        "        self.scores.append(score)",
        "",
        "    def average(self):",
        "        if not self.scores:",
        "            return 0",
        "        return sum(self.scores) / len(self.scores)",
    ]
    if rev >= 2:
        lines += [
            "",
            "    def __str__(self):",
            "        return f'{self.name}({self.student_id})'",
        ]
    if rev >= 3:
        lines += [
            "",
            "    @property",
            "    def grade(self):",
            "        avg = self.average()",
            "        if avg >= 90:",
            "            return 'A'",
            "        if avg >= 80:",
            "            return 'B'",
            "        return 'C'",
        ]
    if rev >= 4:
        lines += [
            "",
            "    def copy_scores(self):",
            "        # 복습: 리스트 복사 주의",
            "        return list(self.scores)",
            "",
            "if __name__ == '__main__':",
            "    s = Student('민수', '2024001')",
            "    s.add_score(88)",
            "    s.add_score(92)",
            "    print(s, s.average(), s.grade)",
            "    print('copy', s.copy_scores())",
        ]
    if rev >= 5:
        lines += [
            "",
            "# 메모: 점수 평균 반올림은 나중에",
        ]
    return nl(*lines)


@register("oop/bank_account.py")
def oop_bank_account(rev: int, _total: int) -> str:
    lines = [
        "class BankAccount:",
        "    def __init__(self, owner, balance=0):",
        "        self.owner = owner",
        "        self.balance = balance",
        "",
        "    def deposit(self, amount):",
        "        if amount <= 0:",
        "            raise ValueError('입금액 오류')",
        "        self.balance += amount",
        "",
        "    def withdraw(self, amount):",
        "        if amount > self.balance:",
        "            raise ValueError('잔액 부족')",
        "        self.balance -= amount",
    ]
    if rev >= 2:
        lines += [
            "",
            "    def __str__(self):",
            "        return f'{self.owner} 잔액 {self.balance:,}원'",
        ]
    if rev >= 3:
        lines += [
            "",
            "class SavingsAccount(BankAccount):",
            "    def __init__(self, owner, balance=0, rate=0.02):",
            "        super().__init__(owner, balance)",
            "        self.rate = rate",
            "",
            "    def add_interest(self):",
            "        interest = int(self.balance * self.rate)",
            "        self.deposit(interest)",
            "        return interest",
        ]
    if rev >= 4:
        lines += [
            "",
            "def transfer(src: BankAccount, dst: BankAccount, amount):",
            "    src.withdraw(amount)",
            "    dst.deposit(amount)",
        ]
    if rev >= 5:
        lines = [
            '"""간단한 은행 계좌 예제 (상속 포함)"""',
            "class BankAccount:",
            "    def __init__(self, owner, balance=0):",
            "        self.owner = owner",
            "        self.balance = balance",
            "",
            "    def deposit(self, amount):",
            "        if amount <= 0:",
            "            raise ValueError('입금액 오류')",
            "        self.balance += amount",
            "",
            "    def withdraw(self, amount):",
            "        if amount > self.balance:",
            "            raise ValueError('잔액 부족')",
            "        self.balance -= amount",
            "",
            "    def __str__(self):",
            "        return f'{self.owner} 잔액 {self.balance:,}원'",
            "",
            "class SavingsAccount(BankAccount):",
            "    def __init__(self, owner, balance=0, rate=0.02):",
            "        super().__init__(owner, balance)",
            "        self.rate = rate",
            "",
            "    def add_interest(self):",
            "        interest = int(self.balance * self.rate)",
            "        self.deposit(interest)",
            "        return interest",
            "",
            "def transfer(src: BankAccount, dst: BankAccount, amount):",
            "    src.withdraw(amount)",
            "    dst.deposit(amount)",
        ]
    if rev >= 6:
        lines += [
            "",
            "class CheckingAccount(BankAccount):",
            "    def __init__(self, owner, balance=0, fee=100):",
            "        super().__init__(owner, balance)",
            "        self.fee = fee",
            "",
            "    def withdraw(self, amount):",
            "        super().withdraw(amount + self.fee)",
            "        return amount",
            "",
            "def print_history(accounts):",
            "    for acc in accounts:",
            "        print('-', acc)",
            "",
            "if __name__ == '__main__':",
            "    acc = SavingsAccount('김학생', 10000)",
            "    acc.deposit(5000)",
            "    chk = CheckingAccount('김학생', 3000)",
            "    try:",
            "        transfer(acc, chk, 2000)",
            "    except ValueError as err:",
            "        print('이체 실패', err)",
            "    print_history([acc, chk])",
            "    print('이자', acc.add_interest())",
        ]
    return nl(*lines)


@register("oop/library.py")
def oop_library(rev: int, _total: int) -> str:
    lines = [
        "class Book:",
        "    def __init__(self, title, author):",
        "        self.title = title",
        "        self.author = author",
        "        self.is_borrowed = False",
        "",
        "    def __str__(self):",
        "        status = '대출중' if self.is_borrowed else '대기'",
        "        return f'{self.title} / {self.author} [{status}]'",
        "",
        "class Library:",
        "    def __init__(self):",
        "        self.books = []",
        "",
        "    def add_book(self, book: Book):",
        "        self.books.append(book)",
    ]
    if rev >= 2:
        lines += [
            "",
            "    def find(self, keyword):",
            "        return [b for b in self.books if keyword in b.title]",
        ]
    if rev >= 3:
        lines += [
            "",
            "    def borrow(self, title):",
            "        for b in self.books:",
            "            if b.title == title and not b.is_borrowed:",
            "                b.is_borrowed = True",
            "                return True",
            "        return False",
        ]
    if rev >= 4:
        lines += [
            "",
            "    def return_book(self, title):",
            "        for b in self.books:",
            "            if b.title == title:",
            "                b.is_borrowed = False",
            "                return True",
            "        return False",
        ]
    if rev >= 5:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    lib = Library()",
            "    lib.add_book(Book('파이썬 입문', '홍길동'))",
            "    lib.add_book(Book('데이터 분석', '이몽룡'))",
            "    print(lib.borrow('파이썬 입문'))",
            "    for b in lib.books:",
            "        print(b)",
        ]
    return nl(*lines)


# --- io ---


@register("io/read_file.py")
def io_read_file(rev: int, _total: int) -> str:
    lines = [
        "# 파일 읽기",
        "from pathlib import Path",
        "",
        "def read_text(path: str) -> str:",
        "    p = Path(path)",
        "    if not p.exists():",
        "        return ''",
        "    return p.read_text(encoding='utf-8')",
        "",
        "if __name__ == '__main__':",
        "    print(read_text('io/memo.txt')[:80])",
    ]
    if rev >= 2:
        lines += [
            "",
            "def read_lines(path: str):",
            "    text = read_text(path)",
            "    return text.splitlines() if text else []",
        ]
    if rev >= 3:
        lines += [
            "",
            "def safe_read(path: str, default=''):",
            "    try:",
            "        return read_text(path)",
            "    except OSError as err:",
            "        print('읽기 실패', err)",
            "        return default",
        ]
    return nl(*lines)


@register("io/write_file.py")
def io_write_file(rev: int, _total: int) -> str:
    lines = [
        "# 파일 쓰기",
        "from pathlib import Path",
        "",
        "def append_line(path: str, line: str):",
        "    p = Path(path)",
        "    p.parent.mkdir(parents=True, exist_ok=True)",
        "    with p.open('a', encoding='utf-8') as f:",
        "        f.write(line.rstrip() + '\\n')",
    ]
    if rev >= 2:
        lines += [
            "",
            "def write_text(path: str, content: str):",
            "    Path(path).write_text(content, encoding='utf-8')",
        ]
    if rev >= 3:
        lines += [
            "",
            "def log_memo(text: str):",
            "    append_line('io/memo.txt', text)",
        ]
    if rev >= 4:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    log_memo('오늘 공부: with 문')",
        ]
    if rev >= 5:
        lines += [
            "",
            "# pathlib 로 경로 통일 연습",
            "BASE = Path('io')",
        ]
    return nl(*lines)


@register("io/csv_demo.py")
def io_csv_demo(rev: int, _total: int) -> str:
    lines = [
        "import csv",
        "from pathlib import Path",
        "",
        "CSV_PATH = Path('io/scores.csv')",
        "",
        "def read_scores():",
        "    if not CSV_PATH.exists():",
        "        return []",
        "    with CSV_PATH.open(encoding='utf-8') as f:",
        "        return list(csv.DictReader(f))",
        "",
        "def average_score(rows):",
        "    if not rows:",
        "        return 0",
        "    total = sum(int(r['score']) for r in rows)",
        "    return total / len(rows)",
    ]
    if rev >= 2:
        lines += [
            "",
            "def append_score(name, score):",
            "    new_file = not CSV_PATH.exists()",
            "    with CSV_PATH.open('a', newline='', encoding='utf-8') as f:",
            "        w = csv.writer(f)",
            "        if new_file:",
            "            w.writerow(['name', 'score'])",
            "        w.writerow([name, score])",
        ]
    if rev >= 3:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    rows = read_scores()",
            "    print('평균', average_score(rows))",
        ]
    if rev >= 4:
        lines += [
            "",
            "def top_student(rows):",
            "    if not rows:",
            "        return None",
            "    return max(rows, key=lambda r: int(r['score']))",
        ]
    if rev >= 5:
        lines += [
            "",
            "    # encoding utf-8 명시 복습",
            "    print('1등', top_student(rows))",
        ]
    if rev >= 6:
        lines += [
            "",
            "def filter_by_min(rows, minimum):",
            "    return [r for r in rows if int(r['score']) >= minimum]",
        ]
    return nl(*lines)


@register("io/json_demo.py")
def io_json_demo(rev: int, _total: int) -> str:
    lines = [
        "import json",
        "from pathlib import Path",
        "",
        "PROFILE = Path('io/profile.json')",
        "",
        "def load_profile():",
        "    if not PROFILE.exists():",
        "        return {}",
        "    return json.loads(PROFILE.read_text(encoding='utf-8'))",
        "",
        "def save_profile(data):",
        "    PROFILE.write_text(",
        "        json.dumps(data, ensure_ascii=False, indent=2),",
        "        encoding='utf-8',",
        "    )",
    ]
    if rev >= 2:
        lines += [
            "",
            "def update_field(key, value):",
            "    data = load_profile()",
            "    data[key] = value",
            "    save_profile(data)",
        ]
    if rev >= 3:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    update_field('last_study', 'json')",
            "    print(load_profile())",
        ]
    if rev >= 4:
        lines += [
            "",
            "def ensure_defaults():",
            "    data = load_profile()",
            "    data.setdefault('hobbies', [])",
            "    data.setdefault('level', 'beginner')",
            "    save_profile(data)",
            "    return data",
        ]
    if rev >= 5:
        lines += [
            "",
            "# 크롤링 결과 저장 연습용",
            "def export_copy(path: str):",
            "    Path(path).write_text(json.dumps(load_profile(), ensure_ascii=False, indent=2), encoding='utf-8')",
        ]
    return nl(*lines)


@register("io/memo.txt")
def io_memo(rev: int, _total: int) -> str:
    base = [
        "2025-03-17 파이썬 파일 입출력 공부",
        "- read / write 연습",
        "- encoding utf-8",
    ]
    extra = [
        "2025-03-21 csv 한 줄 추가 연습",
        "2025-04-03 BeautifulSoup 셀렉터 메모",
        "2025-04-25 pandas 필터 복습",
        "2025-05-06 파일 없을 때 예외 처리",
        "2025-05-11 pathlib 로 경로 정리",
        "2025-05-12 출력 포맷 다듬기",
    ]
    lines = base + extra[: max(0, rev - 1)]
    return nl(*lines)


@register("io/scores.csv")
def io_scores_csv(rev: int, _total: int) -> str:
    rows = [
        "name,score",
        "민수,88",
        "지영,92",
        "현우,76",
    ]
    if rev >= 2:
        rows.append("수진,95")
    if rev >= 3:
        rows.append("태호,81")
    if rev >= 4:
        rows.append("서연,90")
    if rev >= 5:
        rows.append("준호,84")
    return nl(*rows)


@register("io/profile.json")
def io_profile_json(rev: int, _total: int) -> str:
    data = {
        "name": "김학생",
        "level": "beginner",
        "hobbies": ["coding", "walking"],
    }
    if rev >= 2:
        data["last_study"] = "json"
    if rev >= 3:
        data["courses"] = ["basics", "functions", "oop"]
    if rev >= 4:
        data["github"] = "GyeongMin2/pythonLearningHub"
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


# --- analysis ---


@register("analysis/series_practice.py")
def analysis_series_practice(rev: int, _total: int) -> str:
    lines = [
        "# pandas Series 연습",
        "import pandas as pd",
        "",
        "s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])",
        "print(s)",
        "print('mean', s.mean())",
    ]
    if rev >= 2:
        lines += [
            "",
            "print('max idx', s.idxmax())",
            "print('filter > 15', s[s > 15])",
        ]
    return nl(*lines)


@register("analysis/pandas_intro.py")
def analysis_pandas_intro(rev: int, _total: int) -> str:
    lines = [
        "import pandas as pd",
        "from pathlib import Path",
        "",
        "CSV = Path('analysis/weather.csv')",
        "",
        "def load_weather():",
        "    if not CSV.exists():",
        "        return pd.DataFrame()",
        "    return pd.read_csv(CSV, encoding='utf-8')",
        "",
        "def main():",
        "    df = load_weather()",
        "    if df.empty:",
        "        print('데이터 없음')",
        "        return",
        "    print(df.head())",
        "    print('평균 기온', df['temp'].mean())",
    ]
    if rev >= 2:
        lines += [
            "",
            "    rainy = df[df['rain'] > 0]",
            "    print('비 온 날', len(rainy))",
        ]
    if rev >= 3:
        lines += [
            "",
            "    by_city = df.groupby('city')['temp'].mean()",
            "    print(by_city)",
        ]
    if rev >= 4:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    main()",
        ]
    if rev >= 5:
        lines += [
            "",
            "# plot 은 나중에 (matplotlib)",
            "# import matplotlib.pyplot as plt",
            "# df['temp'].plot(kind='line')",
        ]
    if rev >= 6:
        lines += [
            "",
            "def filter_hot(df, threshold=28):",
            "    return df[df['temp'] >= threshold]",
        ]
    return nl(*lines)


@register("analysis/weather_data.py")
def analysis_weather_data(rev: int, _total: int) -> str:
    lines = [
        "import pandas as pd",
        "from pathlib import Path",
        "",
        "DATA = Path('analysis/weather.csv')",
        "",
        "def summarize():",
        "    df = pd.read_csv(DATA, encoding='utf-8')",
        "    print('rows', len(df))",
        "    print(df.describe(include='all'))",
        "    return df",
        "",
        "def monthly_mean(df):",
        "    if 'month' not in df.columns:",
        "        return df",
        "    return df.groupby('month')['temp'].mean()",
    ]
    if rev >= 2:
        lines += [
            "",
            "def save_summary(path: str):",
            "    df = summarize()",
            "    monthly_mean(df).to_csv(path, encoding='utf-8')",
        ]
    if rev >= 3:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    summarize()",
        ]
    if rev >= 4:
        lines += [
            "",
            "def rainy_days(df):",
            "    return df[df['rain'] > 0.0]",
        ]
    if rev >= 5:
        lines += [
            "",
            "def city_stats(df):",
            "    return df.groupby('city').agg({'temp': 'mean', 'rain': 'sum'})",
        ]
    if rev >= 6:
        lines += [
            "",
            "# 리팩터: 함수 이름 정리",
            "def run():",
            "    df = summarize()",
            "    print(city_stats(df))",
        ]
    if rev >= 7:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    run()",
        ]
    return nl(*lines)


@register("analysis/weather.csv")
def analysis_weather_csv(rev: int, _total: int) -> str:
    rows = [
        "date,city,temp,rain,month",
        "2025-03-01,Seoul,5.2,0.0,3",
        "2025-03-02,Seoul,6.1,2.5,3",
        "2025-03-03,Busan,8.0,0.0,3",
        "2025-03-04,Busan,9.5,0.0,3",
    ]
    extras = [
        "2025-03-05,Seoul,7.0,1.0,3",
        "2025-03-06,Daejeon,6.8,0.0,3",
        "2025-04-01,Seoul,14.2,0.0,4",
        "2025-04-02,Busan,15.0,5.2,4",
        "2025-04-03,Incheon,13.5,0.0,4",
        "2025-05-10,Seoul,22.1,0.0,5",
        "2025-05-11,Busan,23.4,0.0,5",
    ]
    rows.extend(extras[: max(0, rev - 1)])
    return nl(*rows)


# --- crawling ---


@register("crawling/requests_intro.py")
def crawling_requests_intro(rev: int, _total: int) -> str:
    lines = [
        "import requests",
        "",
        "HEADERS = {",
        "    'User-Agent': 'Mozilla/5.0 (study-bot; +https://github.com/GyeongMin2/pythonLearningHub)',",
        "}",
        "",
        "def fetch(url: str, timeout=10):",
        "    try:",
        "        resp = requests.get(url, headers=HEADERS, timeout=timeout)",
        "        resp.raise_for_status()",
        "        return resp.text",
        "    except requests.RequestException as err:",
        "        print('요청 실패', err)",
        "        return ''",
    ]
    if rev >= 2:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    html = fetch('https://example.com')",
            "    print('len', len(html))",
        ]
    if rev >= 3:
        lines += [
            "",
            "def fetch_bytes(url: str):",
            "    resp = requests.get(url, headers=HEADERS, timeout=10)",
            "    resp.raise_for_status()",
            "    return resp.content",
        ]
    return nl(*lines)


@register("crawling/bs4_intro.py")
def crawling_bs4_intro(rev: int, _total: int) -> str:
    lines = [
        "from bs4 import BeautifulSoup",
        "",
        "SAMPLE = '''",
        "<html><body><h1>News</h1><a class='title'>Hello</a></body></html>",
        "'''",
        "",
        "def parse_titles(html: str):",
        "    soup = BeautifulSoup(html, 'html.parser')",
        "    return [a.get_text(strip=True) for a in soup.select('a.title')]",
    ]
    if rev >= 2:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    print(parse_titles(SAMPLE))",
        ]
    if rev >= 3:
        lines += [
            "",
            "def parse_headings(html: str):",
            "    soup = BeautifulSoup(html, 'html.parser')",
            "    return [h.get_text(strip=True) for h in soup.find_all('h1')]",
        ]
    if rev >= 4:
        lines += [
            "",
            "def safe_parse(html: str):",
            "    try:",
            "        return parse_titles(html)",
            "    except Exception as err:",
            "        print('파싱 오류', err)",
            "        return []",
        ]
    if rev >= 5:
        lines += [
            "",
            "# json 저장 연습과 연계",
            "def to_rows(titles):",
            "    return [{'title': t} for t in titles]",
        ]
    return nl(*lines)


@register("crawling/news_titles.py")
def crawling_news_titles(rev: int, _total: int) -> str:
    lines = [
        "import csv",
        "from pathlib import Path",
        "import requests",
        "from bs4 import BeautifulSoup",
        "",
        "from crawling.requests_intro import HEADERS",
        "",
        "OUT = Path('crawling/titles.csv')",
        "URL = 'https://example.com/'",
        "",
        "def fetch_html():",
        "    try:",
        "        r = requests.get(URL, headers=HEADERS, timeout=10)",
        "        r.raise_for_status()",
        "        return r.text",
        "    except requests.RequestException as err:",
        "        print('크롤링 실패', err)",
        "        return ''",
        "",
        "def extract_titles(html: str):",
        "    soup = BeautifulSoup(html, 'html.parser')",
        "    titles = [h.get_text(strip=True) for h in soup.find_all('h1')]",
        "    if not titles:",
        "        titles = ['(샘플) Example Domain']",
        "    return titles",
    ]
    if rev >= 2:
        lines += [
            "",
            "def save_csv(titles):",
            "    OUT.parent.mkdir(parents=True, exist_ok=True)",
            "    with OUT.open('w', newline='', encoding='utf-8') as f:",
            "        w = csv.writer(f)",
            "        w.writerow(['title'])",
            "        for t in titles:",
            "            w.writerow([t])",
        ]
    if rev >= 3:
        lines += [
            "",
            "def run():",
            "    html = fetch_html()",
            "    titles = extract_titles(html)",
            "    save_csv(titles)",
            "    print('saved', len(titles))",
        ]
    if rev >= 4:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    run()",
        ]
    if rev >= 5:
        lines += [
            "",
            "def load_saved():",
            "    if not OUT.exists():",
            "        return []",
            "    with OUT.open(encoding='utf-8') as f:",
            "        return list(csv.DictReader(f))",
        ]
    if rev >= 6:
        lines += [
            "",
            "# 셀렉터 수정 메모 — h1 말고 a 태그도 시도",
            "def extract_links(html: str):",
            "    soup = BeautifulSoup(html, 'html.parser')",
            "    return [a.get('href') for a in soup.find_all('a')[:5]]",
        ]
    return nl(*lines)


@register("crawling/titles.csv")
def crawling_titles_csv(rev: int, _total: int) -> str:
    rows = ["title", "(샘플) Example Domain"]
    if rev >= 2:
        rows.append("More information")
    if rev >= 3:
        rows.append("Learn more")
    if rev >= 4:
        rows.append("Python study crawl")
    return nl(*rows)


# --- projects ---


@register("projects/contacts.py")
def projects_contacts(rev: int, _total: int) -> str:
    lines = [
        "import json",
        "from pathlib import Path",
        "",
        "DATA = Path('projects/contacts.json')",
        "",
        "def load():",
        "    if not DATA.exists():",
        "        return []",
        "    try:",
        "        return json.loads(DATA.read_text(encoding='utf-8'))",
        "    except json.JSONDecodeError:",
        "        print('JSON 깨짐 — 빈 목록으로 시작')",
        "        return []",
        "",
        "def save(contacts):",
        "    DATA.parent.mkdir(parents=True, exist_ok=True)",
        "    DATA.write_text(json.dumps(contacts, ensure_ascii=False, indent=2), encoding='utf-8')",
        "",
        "def add_contact(name, phone, email=''):",
        "    contacts = load()",
        "    for c in contacts:",
        "        if c['name'] == name:",
        "            print('이미 있음, 업데이트')",
        "            c['phone'] = phone",
        "            c['email'] = email",
        "            save(contacts)",
        "            return",
        "    contacts.append({'name': name, 'phone': phone, 'email': email})",
        "    save(contacts)",
    ]
    if rev >= 2:
        lines += [
            "",
            "def find_contact(keyword):",
            "    keyword = keyword.strip().lower()",
            "    for c in load():",
            "        if keyword in c['name'].lower():",
            "            return c",
            "    return None",
            "",
            "def list_contacts():",
            "    contacts = load()",
            "    if not contacts:",
            "        print('연락처 없음')",
            "        return",
            "    for i, c in enumerate(contacts, 1):",
            "        email = c.get('email') or '-'",
            "        print(f\"{i}. {c['name']} / {c['phone']} / {email}\")",
        ]
    if rev >= 3:
        lines += [
            "",
            "def delete_contact(name):",
            "    contacts = load()",
            "    new_list = [c for c in contacts if c['name'] != name]",
            "    if len(new_list) == len(contacts):",
            "        print('없는 이름')",
            "        return False",
            "    save(new_list)",
            "    return True",
        ]
    if rev >= 4:
        lines += [
            "",
            "def search_contacts(keyword):",
            "    keyword = keyword.strip().lower()",
            "    return [c for c in load() if keyword in c['name'].lower() or keyword in c['phone']]",
        ]
    if rev >= 5:
        lines += [
            "",
            "def normalize_phone(phone: str) -> str:",
            "    digits = ''.join(ch for ch in phone if ch.isdigit())",
            "    if len(digits) < 10:",
            "        raise ValueError('전화번호 짧음')",
            "    return phone.strip()",
            "",
            "def export_backup(path: str = 'projects/contacts_backup.json'):",
            "    Path(path).write_text(json.dumps(load(), ensure_ascii=False, indent=2), encoding='utf-8')",
            "    print('백업 저장', path)",
            "",
            "def menu():",
            "    while True:",
            "        print('1 추가 2 검색 3 목록 4 삭제 5 백업 0 종료')",
            "        choice = input('> ').strip()",
            "        if choice == '0':",
            "            break",
            "        if choice == '1':",
            "            name = input('이름: ').strip()",
            "            if not name:",
            "                print('이름 필요')",
            "                continue",
            "            phone = input('전화: ').strip()",
            "            email = input('email(선택): ').strip()",
            "            try:",
            "                phone = normalize_phone(phone)",
            "            except ValueError as err:",
            "                print(err)",
            "                continue",
            "            add_contact(name, phone, email)",
            "        elif choice == '2':",
            "            key = input('검색: ').strip()",
            "            found = search_contacts(key)",
            "            if not found:",
            "                print('결과 없음')",
            "            for c in found:",
            "                print(c)",
            "        elif choice == '3':",
            "            list_contacts()",
            "        elif choice == '4':",
            "            name = input('삭제할 이름: ').strip()",
            "            delete_contact(name)",
            "        elif choice == '5':",
            "            export_backup()",
            "        else:",
            "            print('다시 선택')",
            "",
            "if __name__ == '__main__':",
            "    menu()",
        ]
    return nl(*lines)


@register("projects/contacts.json")
def projects_contacts_json(rev: int, _total: int) -> str:
    contacts = [
        {"name": "민수", "phone": "010-1111-2222", "email": "minsu@example.com"},
        {"name": "지영", "phone": "010-3333-4444", "email": ""},
    ]
    if rev >= 2:
        contacts.append({"name": "현우", "phone": "010-5555-6666", "email": "hyun@example.com"})
    if rev >= 3:
        contacts[0]["phone"] = "010-1111-9999"
    if rev >= 4:
        contacts.append({"name": "서연", "phone": "010-7777-8888", "email": "seoyeon@example.com"})
    return json.dumps(contacts, ensure_ascii=False, indent=2) + "\n"


@register("projects/weather_collector.py")
def projects_weather_collector(rev: int, total: int) -> str:
    lines = [
        '"""날씨 수집기 — CSV 로그 + (선택) API/스크래핑 스텁"""',
        "import csv",
        "import logging",
        "from datetime import datetime",
        "from pathlib import Path",
        "",
        "try:",
        "    import requests",
        "except ImportError:",
        "    requests = None",
        "",
        "LOG = Path('projects/weather_log.csv')",
        "REPORT = Path('projects/weather_report.txt')",
        "API_URL = 'https://api.example.com/weather'  # placeholder",
        "",
        "logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')",
        "logger = logging.getLogger('weather')",
        "",
        "HEADERS = {",
        "    'User-Agent': 'pythonLearningHub-study/1.0',",
        "}",
        "",
        "def init_log():",
        "    if LOG.exists():",
        "        return",
        "    LOG.parent.mkdir(parents=True, exist_ok=True)",
        "    with LOG.open('w', newline='', encoding='utf-8') as f:",
        "        csv.writer(f).writerow(['date', 'city', 'temp', 'rain', 'source'])",
    ]
    if rev >= 2:
        lines += [
            "",
            "def append_row(city, temp, rain=0.0, source='manual'):",
            "    init_log()",
            "    day = datetime.now().strftime('%Y-%m-%d')",
            "    with LOG.open('a', newline='', encoding='utf-8') as f:",
            "        csv.writer(f).writerow([day, city, temp, rain, source])",
            "    logger.info('saved %s %s', city, temp)",
        ]
    if rev >= 3:
        lines += [
            "",
            "def load_rows():",
            "    if not LOG.exists():",
            "        return []",
            "    with LOG.open(encoding='utf-8') as f:",
            "        return list(csv.DictReader(f))",
        ]
    if rev >= 4:
        lines += [
            "",
            "def summary():",
            "    rows = load_rows()",
            "    if not rows:",
            "        print('데이터 없음')",
            "        return",
            "    temps = [float(r['temp']) for r in rows]",
            "    rainy = [r for r in rows if float(r.get('rain', 0)) > 0]",
            "    print(f\"{len(rows)}건, 평균기온 {sum(temps)/len(temps):.1f}\")",
            "    print(f'비 온 기록 {len(rainy)}건')",
        ]
    if rev >= 5:
        lines += [
            "",
            "def fetch_api(city: str):",
            "    if requests is None:",
            "        logger.warning('requests 없음 — 더미 반환')",
            "        return {'city': city, 'temp': 20.0, 'rain': 0.0}",
            "    try:",
            "        # 실제 키 없어서 placeholder",
            "        resp = requests.get(API_URL, params={'city': city}, headers=HEADERS, timeout=8)",
            "        resp.raise_for_status()",
            "        data = resp.json()",
            "        return data",
            "    except Exception as err:",
            "        logger.error('API 실패 %s', err)",
            "        return {'city': city, 'temp': 18.0, 'rain': 0.0, 'source': 'fallback'}",
        ]
    if rev >= 6:
        lines += [
            "",
            "def collect_city(city: str):",
            "    data = fetch_api(city)",
            "    temp = float(data.get('temp', 0))",
            "    rain = float(data.get('rain', 0))",
            "    source = data.get('source', 'api')",
            "    append_row(city, temp, rain, source)",
            "",
            "def scrape_stub(city: str):",
            "    # BeautifulSoup 으로 확장 예정",
            "    logger.info('scrape stub for %s', city)",
            "    append_row(city, 19.5, 0.0, 'scrape-stub')",
        ]
    if rev >= 7:
        lines += [
            "",
            "def write_report():",
            "    rows = load_rows()",
            "    lines_out = ['=== weather report ===']",
            "    for r in rows[-10:]:",
            "        lines_out.append(f\"{r['date']} {r['city']} {r['temp']}C rain={r['rain']}\")",
            "    REPORT.write_text('\\n'.join(lines_out) + '\\n', encoding='utf-8')",
        ]
    if rev >= 8:
        lines += [
            "",
            "def filter_by_city(city: str):",
            "    return [r for r in load_rows() if r['city'].lower() == city.lower()]",
        ]
    if rev >= 9:
        lines += [
            "",
            "def cli():",
            "    print('1 수동입력 2 API수집 3 요약 4 리포트 0 종료')",
            "    while True:",
            "        choice = input('> ').strip()",
            "        if choice == '0':",
            "            break",
            "        if choice == '1':",
            "            city = input('도시: ').strip() or 'Seoul'",
            "            temp = float(input('기온: ').strip() or '20')",
            "            rain = float(input('강수: ').strip() or '0')",
            "            append_row(city, temp, rain, 'manual')",
            "        elif choice == '2':",
            "            city = input('도시: ').strip() or 'Seoul'",
            "            collect_city(city)",
            "        elif choice == '3':",
            "            summary()",
            "        elif choice == '4':",
            "            write_report()",
            "            print('saved', REPORT)",
            "        else:",
            "            print('다시')",
        ]
    if rev >= 10:
        lines += [
            "",
            "def export_txt(path: str = 'projects/weather_export.txt'):",
            "    rows = load_rows()",
            "    Path(path).write_text('\\n'.join(str(r) for r in rows), encoding='utf-8')",
        ]
    if rev >= 11:
        lines += [
            "",
            "def validate_row(row: dict) -> bool:",
            "    try:",
            "        float(row['temp'])",
            "        float(row.get('rain', 0))",
            "        return bool(row.get('city'))",
            "    except (KeyError, ValueError):",
            "        return False",
            "",
            "def clean_log():",
            "    rows = [r for r in load_rows() if validate_row(r)]",
            "    init_log()",
            "    with LOG.open('w', newline='', encoding='utf-8') as f:",
            "        w = csv.writer(f)",
            "        w.writerow(['date', 'city', 'temp', 'rain', 'source'])",
            "        for r in rows:",
            "            w.writerow([r['date'], r['city'], r['temp'], r['rain'], r.get('source', '')])",
            "    logger.info('cleaned %s rows', len(rows))",
            "",
            "if __name__ == '__main__':",
            "    # 테스트 데이터",
            "    if not LOG.exists():",
            "        append_row('Seoul', 22.0, 0.0, 'seed')",
            "        append_row('Busan', 24.5, 1.2, 'seed')",
            "    clean_log()",
            "    cli()",
            f"    # rev {rev}/{total} — 프로젝트 마무리",
        ]
    return nl(*lines)


@register("projects/todo.py")
def projects_todo(rev: int, _total: int) -> str:
    lines = [
        "import json",
        "from pathlib import Path",
        "",
        "STORE = Path('projects/todos.json')",
        "",
        "def load():",
        "    if not STORE.exists():",
        "        return []",
        "    return json.loads(STORE.read_text(encoding='utf-8'))",
        "",
        "def save(items):",
        "    STORE.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')",
        "",
        "def add_task(title):",
        "    items = load()",
        "    items.append({'title': title, 'done': False})",
        "    save(items)",
    ]
    if rev >= 2:
        lines += [
            "",
            "def toggle(title):",
            "    items = load()",
            "    for t in items:",
            "        if t['title'] == title:",
            "            t['done'] = not t['done']",
            "    save(items)",
        ]
    if rev >= 3:
        lines += [
            "",
            "def list_tasks():",
            "    for t in load():",
            "        mark = 'x' if t['done'] else ' '",
            "        print(f'[{mark}] {t[\"title\"]}')",
        ]
    if rev >= 4:
        lines += [
            "",
            "if __name__ == '__main__':",
            "    add_task('pandas 복습')",
            "    list_tasks()",
        ]
    if rev >= 5:
        lines += [
            "",
            "def menu():",
            "    while True:",
            "        print('1 add 2 toggle 3 list 0 quit')",
            "        c = input('> ').strip()",
            "        if c == '0':",
            "            break",
            "        if c == '1':",
            "            add_task(input('title: ').strip())",
            "        elif c == '2':",
            "            toggle(input('title: ').strip())",
            "        elif c == '3':",
            "            list_tasks()",
        ]
    return nl(*lines)


@register("projects/todos.json")
def projects_todos_json(rev: int, _total: int) -> str:
    items = [
        {"title": "contacts CLI 마무리", "done": False},
        {"title": "weather collector 테스트", "done": False},
    ]
    if rev >= 2:
        items[0]["done"] = True
    if rev >= 3:
        items.append({"title": "readme 정리", "done": False})
    if rev >= 4:
        items[1]["done"] = True
    if rev >= 5:
        items.append({"title": "6개월 회고 작성", "done": False})
    return json.dumps(items, ensure_ascii=False, indent=2) + "\n"


@register("projects/weather_log.csv")
def projects_weather_log(rev: int, _total: int) -> str:
    rows = ["date,city,temp,rain,source", "2025-05-20,Seoul,21.0,0.0,manual"]
    extras = [
        "2025-05-21,Busan,23.5,0.0,manual",
        "2025-05-23,Seoul,19.0,3.0,manual",
        "2025-06-01,Seoul,25.0,0.0,api",
        "2025-06-10,Busan,26.2,0.0,api",
    ]
    rows.extend(extras[: max(0, rev - 1)])
    return nl(*rows)


@register("projects/weather_report.txt")
def projects_weather_report(rev: int, _total: int) -> str:
    lines = [
        "=== weather report ===",
        "2025-05-20 Seoul 21.0C rain=0.0",
    ]
    if rev >= 2:
        lines.append("2025-05-21 Busan 23.5C rain=0.0")
    if rev >= 3:
        lines += [
            "요약: 서울 평균 20.3 / 부산 24.8",
            "비 온 날: 1",
        ]
    return nl(*lines)


@register("projects/readme_notes.md")
def projects_readme_notes(rev: int, _total: int) -> str:
    lines = [
        "# 6개월 파이썬 미니 프로젝트 메모",
        "",
        "## contacts",
        "- JSON 저장/불러오기",
        "- CRUD + 검색",
        "",
        "## weather_collector",
        "- CSV 로그",
        "- API placeholder",
    ]
    if rev >= 2:
        lines += ["", "- logging 추가"]
    if rev >= 3:
        lines += ["- todo.py 는 연습용"]
    if rev >= 4:
        lines += ["", "## 다음", "- matplotlib 그래프 (시간되면)"]
    return nl(*lines)


def build_content(path: str, rev: int, total: int) -> str:
    builder = BUILDERS.get(path)
    if not builder:
        raise KeyError(f"no builder for {path}")
    return builder(rev, total)


def main() -> None:
    with SKELETON.open(encoding="utf-8") as f:
        skeleton = json.load(f)

    totals: dict[str, int] = {}
    for entry in skeleton:
        for p in entry["files"]:
            totals[p] = totals.get(p, 0) + 1

    rev_counter: dict[str, int] = {}
    out = []
    for entry in skeleton:
        files_out = {}
        for path in entry["files"]:
            rev_counter[path] = rev_counter.get(path, 0) + 1
            files_out[path] = build_content(path, rev_counter[path], totals[path])
        out.append({"date": entry["date"], "message": entry["message"], "files": files_out})

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(out)} commits -> {OUT}")


if __name__ == "__main__":
    main()
