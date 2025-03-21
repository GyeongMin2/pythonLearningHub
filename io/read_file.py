# 파일 읽기
from pathlib import Path

def read_text(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return ''
    return p.read_text(encoding='utf-8')

if __name__ == '__main__':
    print(read_text('io/memo.txt')[:80])

def read_lines(path: str):
    text = read_text(path)
    return text.splitlines() if text else []
