# 파일 쓰기
from pathlib import Path

def append_line(path: str, line: str):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('a', encoding='utf-8') as f:
        f.write(line.rstrip() + '\n')

def write_text(path: str, content: str):
    Path(path).write_text(content, encoding='utf-8')

def log_memo(text: str):
    append_line('io/memo.txt', text)
