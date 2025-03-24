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
