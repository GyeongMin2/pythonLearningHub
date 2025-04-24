import csv
from pathlib import Path

CSV_PATH = Path('io/scores.csv')

def read_scores():
    if not CSV_PATH.exists():
        return []
    with CSV_PATH.open(encoding='utf-8') as f:
        return list(csv.DictReader(f))

def average_score(rows):
    if not rows:
        return 0
    total = sum(int(r['score']) for r in rows)
    return total / len(rows)

def append_score(name, score):
    new_file = not CSV_PATH.exists()
    with CSV_PATH.open('a', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(['name', 'score'])
        w.writerow([name, score])

if __name__ == '__main__':
    rows = read_scores()
    print('평균', average_score(rows))

def top_student(rows):
    if not rows:
        return None
    return max(rows, key=lambda r: int(r['score']))
