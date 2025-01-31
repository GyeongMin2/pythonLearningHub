"""자주 쓰는 유틸 함수 모음"""

def is_even(n: int) -> bool:
    return n % 2 == 0

def clamp(n, lo, hi):
    return max(lo, min(hi, n))
