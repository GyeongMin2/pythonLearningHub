# 파일 쓰기
from pathlib import Path

def append_line(path: str, line: str):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('a', encoding='utf-8') as f:
        f.write(line.rstrip() + '\n')
