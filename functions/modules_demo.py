"""모듈 import 연습"""
import math
from datetime import date

print('pi', round(math.pi, 4))
print('오늘', date.today())

import random
print('주사위', random.randint(1, 6))

from pathlib import Path
here = Path(__file__).resolve().parent
print('경로', here)

def circle_area(r):
    return math.pi * r * r

import json
sample = {'topic': 'modules', 'ok': True}
print(json.dumps(sample, ensure_ascii=False))

def demo():
    print('demo', circle_area(3))

if __name__ == '__main__':
    demo()
    # 가독성 개선 메모
