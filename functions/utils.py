"""자주 쓰는 유틸 함수 모음"""

def is_even(n: int) -> bool:
    return n % 2 == 0

def clamp(n, lo, hi):
    return max(lo, min(hi, n))

def average(nums):
    if not nums:
        raise ValueError('빈 리스트')
    return sum(nums) / len(nums)

def unique(seq):
    seen = []
    for x in seq:
        if x not in seen:
            seen.append(x)
    return seen

def read_lines(path):
    try:
        with open(path, encoding='utf-8') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def slugify(text: str) -> str:
    return text.strip().lower().replace(' ', '-')

if __name__ == '__main__':
    print(average([1, 2, 3]))
    print(unique([1, 1, 2, 3, 2]))
    # 복습 메모 rev 6
