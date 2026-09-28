import json
from pathlib import Path

PROFILE = Path('io/profile.json')

def load_profile():
    if not PROFILE.exists():
        return {}
    return json.loads(PROFILE.read_text(encoding='utf-8'))

def save_profile(data):
    PROFILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding='utf-8',
    )

def update_field(key, value):
    data = load_profile()
    data[key] = value
    save_profile(data)

if __name__ == '__main__':
    update_field('last_study', 'json')
    print(load_profile())

def ensure_defaults():
    data = load_profile()
    data.setdefault('hobbies', [])
    data.setdefault('level', 'beginner')
    save_profile(data)
    return data

# 크롤링 결과 저장 연습용
def export_copy(path: str):
    Path(path).write_text(json.dumps(load_profile(), ensure_ascii=False, indent=2), encoding='utf-8')
